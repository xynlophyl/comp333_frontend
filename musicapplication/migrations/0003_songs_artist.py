# Generated by Django 4.0.2 on 2022-04-11 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapplication', '0002_ratings_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='artist',
            field=models.CharField(default='null', max_length=255),
            preserve_default=False,
        ),
    ]
