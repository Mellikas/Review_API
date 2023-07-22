# Generated by Django 4.2.3 on 2023-07-21 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postit_api', '0003_alter_albumreviewcomment_album_review_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='albumreview',
            name='image',
            field=models.ImageField(null=True, upload_to='pictures'),
        ),
        migrations.AlterField(
            model_name='albumreviewlike',
            name='album_review_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='postit_api.albumreview'),
        ),
    ]
