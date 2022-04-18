from re import T
from unittest.util import _MAX_LENGTH
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

class user (models.Model):
    username = models.CharField(max_length=255, primary_key=True)
    password = models.CharField(max_length=255)
    def __str__(self):
        return self.username

class rating (models.Model):
    username = models.ForeignKey(user, on_delete=models.CASCADE)
    song_artist = models.CharField(max_length=255)
    song = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    rating = models.PositiveBigIntegerField(validators= [MinValueValidator(0), MaxValueValidator(5)])
    def __str__(self):
       return f'{self.song} -> {self.rating}'


class song (models.Model) :
    #fields: song_artist, song, artist, genre
    GENRE = (('Pop','Pop'), ('Hip-Hop','Hip-Hop'), ('Classic','Classic'), ('Rock','Rock'), ('Country','Country'))
    song_artist = models.CharField(max_length=255, primary_key=True)
    song = models.CharField(max_length=255)#, primary_key=True)
    artist = models.CharField(max_length=255)
    genre =  models.CharField(max_length=60,choices=GENRE)

    def __str__(self):
        return self.song_artist
    
    def get_rating_average(r):
        if r:
            return sum(r)//len(r)
        return 0
    rating_average = get_rating_average(rating.objects.filter(song_artist=song_artist).values_list('rating', flat=True))
    