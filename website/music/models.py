from django.db import models
from django.urls import reverse

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_tittle = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self})

    def __str__(self):
        return self.album_tittle + ' - ' + self.artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete= models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_tittle = models.CharField(max_length=250)


    def __str__(self):
        return self.song_tittle

