from django.db import models

# Create your models here.    
    
class Thaat(models.Model):
    thaat_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.thaat_name

class Artist(models.Model):
    artist_name = models.CharField(max_length=200)
    gharana = models.CharField(max_length=200)
    
    def __str__(self):
        return self.artist_name    
    
class Raga(models.Model):
    raga_name = models.CharField(max_length=200)
    tht = models.ForeignKey(Thaat)
    
    def __str__(self):
        return self.raga_name
    
class Bandish(models.Model):
    bandish_title = models.CharField(max_length=200)
    rg = models.ForeignKey(Raga)
    original_composer = models.ForeignKey(Artist)
    
    def __str__(self):
        return self.bandish_title
    
class FilmSong(models.Model):
    song_name = models.CharField(max_length=200)
    rg = models.ForeignKey(Raga)
    film = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    
    def __str__(self):
        return self.song_name
    
class Recording(models.Model):
    artist = models.ForeignKey(Artist)
    pub_date = models.DateField('date published')
    
    def __str__(self):
        return self.pub_date