from django.db import models

class Video(models.Model):
    width = models.SmallIntegerField()
    height = models.SmallIntegerField()
    duration = models.TimeField()
    type = models.CharField(max_length=64)
    uri = models.URLField(max_length=512)
    def __unicode__(self):
        return self.uri

class Subtitle(models.Model):
    video = models.ForeignKey(Video)
    language = models.CharField(max_length=8)
    uri = models.URLField(max_length=512)
    def __unicode__(self):
        return self.uri

class Movie(models.Model):
    title = models.CharField(max_length=512)
    date = models.DateField()
    rating = models.CharField(max_length=16)
    description = models.TextField()
    cover = models.URLField(max_length=512)
    video = models.ForeignKey(Video)
    def __unicode__(self):
        return self.title

class TVShow(models.Model):
    title = models.CharField(max_length=512)
    startDate = models.DateField()
    endDate = models.DateField()
    description = models.TextField()
    cover = models.URLField(max_length=512)
    def __unicode__(self):
        return self.title

class Episode(models.Model):
    tvShow = models.ForeignKey(TVShow)
    title = models.CharField(max_length=512)
    date = models.DateField()
    rating = models.CharField(max_length=16)
    epNum = models.SmallIntegerField()
    season = models.SmallIntegerField()
    description = models.TextField()
    video = models.ForeignKey(Video)
    def __unicode__(self):
        return self.title
