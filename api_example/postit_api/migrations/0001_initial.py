# Generated by Django 4.2.3 on 2023-07-19 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='AlbumReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_content', models.CharField(max_length=1000)),
                ('score', models.IntegerField(max_length=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('album_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postit_api.album')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=1000)),
                ('duration', models.CharField(max_length=1000)),
                ('album_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postit_api.album')),
            ],
        ),
        migrations.CreateModel(
            name='AlbumReviewLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('album_review_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postit_api.albumreview')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='AlbumReviewComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.CharField(max_length=1000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('album_review_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postit_api.albumreview')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='album',
            name='band_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postit_api.band'),
        ),
    ]