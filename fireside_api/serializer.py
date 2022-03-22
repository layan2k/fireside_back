"""Serializers for data conversion"""
from rest_framework import serializers

from fireside_api.models import Movie, Profile


class MovieSerializer(serializers.ModelSerializer):
    """Serializes  Movie data from complex data to json and vice versa. """
    class Meta:
        model = Movie
        fields = (
            'title',
            'description',
            'date_created',
            'uuid',
            'movie_type',
            'genre',
            'videos',
            'flyer',
            'thumbnail',
            'age_limit',
            'get_flyer',
            'get_thumbnail',
            'get_movies',
        )


class ProfileSerializer(serializers.ModelSerializer):
    """Serializes Profile data from complex data to json and vice versa. """
    class Meta:
        model = Profile
        fields = "__all__"
