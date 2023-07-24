from rest_framework.exceptions import ValidationError
from .models import Band, Album, Song, AlbumReview, AlbumReviewComment, AlbumReviewLike
from .serializers import BandSerializer, AlbumReviewSerializer, AlbumSerializer, SongSerializer, \
    AlbumReviewCommentSerializer, AlbumReviewLikeSerializer, UserSerializer
from rest_framework import generics, permissions, mixins, status
from rest_framework.response import Response
from django.contrib.auth.models import User


# Create your views here.

class BandList(generics.ListAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AlbumList(generics.ListAPIView):
    # queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        band = Band.objects.get(pk=self.kwargs['pk'])
        return Album.objects.filter(band_id=band)


class SongList(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        album = Album.objects.get(pk=self.kwargs['pk'])
        return Song.objects.filter(album_id=album)


class AlbumReviewList(generics.ListCreateAPIView):
    queryset = AlbumReview.objects.all()
    serializer_class = AlbumReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AlbumReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AlbumReview.objects.all()
    serializer_class = AlbumReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        album_review = AlbumReview.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if album_review.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError('Do not delete others messages!')

    def put(self, request, *args, **kwargs):
        album_review = AlbumReview.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if album_review.exists():
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError("Don't edit others posts!")


class AlbumReviewCommentList(generics.ListCreateAPIView):  # viewsets.ModelViewSet,
    queryset = AlbumReviewComment.objects.all()
    serializer_class = AlbumReviewCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        album_review = AlbumReview.objects.get(pk=self.kwargs['pk'])
        serializer.save(user=self.request.user, album_review_id=album_review)

    def get_queryset(self):
        album_review = AlbumReview.objects.get(pk=self.kwargs['pk'])
        return AlbumReviewComment.objects.filter(album_review_id=album_review)


class AlbumReviewCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AlbumReviewComment.objects.all()
    serializer_class = AlbumReviewCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        album_review_comment = AlbumReviewComment.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if album_review_comment.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError('Do not delete others comments!')

    def put(self, request, *args, **kwargs):
        album_review_comment = AlbumReviewComment.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if album_review_comment.exists():
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError("Don't edit others comments!")


class AlbumReviewLikeCreat(generics.CreateAPIView, mixins.DestroyModelMixin):
    serializer_class = AlbumReviewLikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        album_review = AlbumReview.objects.get(pk=self.kwargs['pk'])
        return AlbumReviewLike.objects.filter(album_review_id=album_review, user=user)

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError('You have already liked this post!')
        album_review = AlbumReview.objects.get(pk=self.kwargs['pk'])
        serializer.save(user=self.request.user, album_review_id=album_review)

    def delete(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError('You have not left a like on this message!')


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def delete(self, request, *args, **kwargs):
        user = User.objects.filter(pk=self.request.user.pk)
        if user.exists():
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError('User doesn\'t exist.')
