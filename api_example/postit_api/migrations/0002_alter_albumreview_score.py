# Generated by Django 4.2.3 on 2023-07-19 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postit_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumreview',
            name='score',
            field=models.IntegerField(),
        ),
    ]
