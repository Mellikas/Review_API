from rest_framework import serializers
from .models import Band, Album, Song, AlbumReview, AlbumReviewComment, AlbumReviewLike
from django.contrib.auth.models import User


class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = ['id', 'band_name']


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'band_id', 'album_name']


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'album_id', 'song_name', 'duration', ]


class AlbumReviewCommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    album_review = serializers.ReadOnlyField(source='albumreview.id')

    class Meta:
        model = AlbumReviewComment
        fields = ['id', 'user', 'user_id', 'album_review_id', 'comment_content', 'created', 'album_review']


class AlbumReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')
    comment_count = serializers.SerializerMethodField()
    comments = serializers.StringRelatedField(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()
    likes = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = AlbumReview
        fields = ['id', 'user', 'user_id', 'album_id', 'review_content', 'score', 'created', 'comments',
                  'comment_count', 'likes', 'likes_count', 'image']

    def get_comment_count(self, obj):
        return AlbumReviewComment.objects.filter(album_review_id=obj).count()

    def get_likes_count(self, obj):
        return AlbumReviewLike.objects.filter(album_review_id=obj).count()


class AlbumReviewLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumReviewLike
        fields = ['id', 'created']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user