# Generated by Django 4.0.2 on 2022-04-18 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapplication', '0014_song_id_alter_song_song_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='song_artist',
            field=models.CharField(max_length=255),
        ),
    ]
