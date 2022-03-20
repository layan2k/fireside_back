"""Serializers for data conversion"""
from rest_framework import serializers

from fireside_api.models import Movie, Profile


class MovieSerializer(serializers.ModelSerializer):
    """Serializes  Movie data from complex data to json and vice versa. """
    class Meta:
        model = Movie
        fields = (
            'uuid',
            'title',
            'description',
            'date_created',
            'movie_type',
            'genre',
            'age_limit',
            'get_flyer',
            'get_thumbnail',
            'get_movies',
            'videos',
        )


class ProfileSerializer(serializers.ModelSerializer):
    """Serializes Profile data from complex data to json and vice versa. """
    class Meta:
        model = Profile
        fields = "__all__"
