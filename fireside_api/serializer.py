"""Serializers for data conversion"""
from rest_framework import serializers

from fireside_api.models import *


class MovieSerializer(serializers.ModelSerializer):
    """Serializes  Movie data from complex data to json and vice versa. """
    class Meta:
        model = Movie
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    """Serializes Profile data from complex data to json and vice versa. """
    class Meta:
        model = Profile
        fields = "__all__"

