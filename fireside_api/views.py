from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from fireside_api.models import Movie
from fireside_api.serializer import MovieSerializer

# Create your views here.

class MovieList(APIView):
    def get(self, request):
        movie= Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)
        return Response(serializer.data)