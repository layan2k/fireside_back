"""Database Models for the movie API """
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser

AGE_CHOICES = {
    ('All', 'All'),
    ('Kids', 'Kids')
}

MOVIE_CHOICES = {
    ('seasonal', 'Seasonal'),
    ('single', 'Single')
}


class CustomUser(AbstractUser):
    """Profile Relation Model"""
    profiles = models.ManyToManyField('Profile', blank=True)


class Profile(models.Model):
    """ Profile Model"""
    name = models.CharField(max_length=225)
    age_limit = models.CharField(max_length=10, choices=AGE_CHOICES)
    uuid = models.UUIDField(default=uuid4)


class Movie(models.Model):
    """Move Model"""
    title = models.CharField(max_length=225)
    description = models.TextField(blank=True, null=True)
    create = models.DateTimeField()
    uuid = models.UUIDField(default=uuid4)
    type = models.CharField(max_length=10, choices=MOVIE_CHOICES)
    videos = models.ManyToManyField('Video')
    flyer = models.ImageField(upload_to='flyers')
    age_limit = models.CharField(max_length=10, choices=AGE_CHOICES)


class Video(models.Model):
    """Video Model"""
    title = models.CharField(max_length=225, blank=True, null=True)
    file = models.FileField(upload_to="movies")
