from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Band(models.Model):
    band_name = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.band_name}"

class Album(models.Model):
    band_id = models.ForeignKey(Band, on_delete=models.CASCADE)
    album_name = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.band_id} '{self.album_name}'"

class Song(models.Model):
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=1000)
    duration = models.CharField(max_length=1000)

    def __str__(self):
        return f"'album:{self.album_id}' song:{self.album_id}' {self.duration}"

class AlbumReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)
    review_content = models.CharField(max_length=1000)
    score = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='album_covers', null=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"ID: {self.id} | '{self.review_content}'"

class AlbumReviewComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album_review_id = models.ForeignKey(AlbumReview, on_delete=models.CASCADE, related_name='comments')
    comment_content = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"coment ID: {self.id} | user: {self.user} | content:'{self.comment_content}' "

class AlbumReviewLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album_review_id = models.ForeignKey(AlbumReview, on_delete=models.CASCADE, related_name='likes')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"user: {self.user} '{self.album_review_id}' date: {self.created}"