"""Database Models for the movie API """
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser
from io import BytesIO
from PIL import Image
from django.core.files import File

AGE_CHOICES = {
    ('All', 'All'),
    ('Kids', 'Kids')
}

MOVIE_CHOICES = {
    ('seasonal', 'Seasonal'),
    ('single', 'Single')
}

GENRE_CHOICES = {
        ('action', 'Action'),
        ('drama', 'Drama'),
        ('horror', 'Horror'),
        ('comedy', 'Comedy'),
        ('fiction', 'Fiction'),
        ('romance', 'Romance'),
        ('documentary', 'Documentary'),
        ('animation', 'Animation'),
        ('fantasy', 'Fantasy'),
        ('sports', 'Sports'),
        ('spirituality', 'Spirituality')
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
    """Movie Model"""
    title = models.CharField(max_length=225)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid4)
    movie_type = models.CharField(max_length=10, choices=MOVIE_CHOICES)
    genre = models.CharField(choices=GENRE_CHOICES, max_length=50)
    videos = models.ManyToManyField('Video')
    flyer = models.ImageField(upload_to='flyers')

    # thumbnail is flyer converted to cute images for display
    thumbnail = models.ImageField(upload_to='flyers/thumbnail',
                                  blank=True, null=True)
    age_limit = models.CharField(max_length=10, choices=AGE_CHOICES)


class Meta:
    """fresh movies displayed first"""
    ordering = ('-date_created',)

    def __str__(self):
        """"string representation"""
        return self.title

    def get_flyer(self):
        """easy access to flyer url"""
        if self.flyer:
            return ('http://127.0.0.1:8000' + self.flyer.url)
        return ''

    def get_thumbnail(self):
        """easy access to thumbnail url"""
        if self.thumbnail:
            return ('http://127.0.0.1:8000' + self.thumbnail.url)
        else:
            if self.flyer:
                self.thumbnail = self.make_thumbnail(self.flyer)
                self.save()
                return ('http://127.0.0.1:8000' + self.thumbnail.url)
            return ''

    def create_thumbnail(self, flyer, size=(300, 200)):
        """create thumbnail from flyer"""
        img = Image.open(flyer)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=100, subsampling=0)

        thumbnail = File(thumb_io, name=flyer.name)
        return thumbnail

    def get_movies(self):
        """easy access to video url as a list"""
        if self.videos:
            return [video.get_video() for video in self.videos.all()]
        return ''


class Video(models.Model):
    """Video Model"""
    title = models.CharField(max_length=225, blank=True, null=True)
    file = models.FileField(upload_to="movies")

    def __str__(self):
        """string representation"""
        return self.title

    def get_video(self):
        """easy access to each video url"""
        if self.file:
            return ('http://127.0.0.1:8000' + self.file.url)
        return ''
