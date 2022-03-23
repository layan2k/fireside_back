"""
Views and logic for the fireside REST API
"""
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from fireside_api.models import Movie
from fireside_api.serializer import MovieSerializer, ProfileSerializer
from .models import Profile, Movie
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q


class MovieList(APIView):
    permission_classes = [IsAuthenticated]
    """Movies Route"""
    def get(self, request):
        """
        GET all movies from the endpoint
        /api/video/
        """
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)
        return Response(serializer.data)


class ProfileList(APIView):
    permission_classes = [IsAuthenticated]
    """Profile List Route"""
    def get(self, request):
        """
        GET Profile objects in db
        endpoint /api/profile/
        """
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)


class ProfileCreate(APIView):
    permission_classes = [IsAuthenticated]
    """Create Profile Route"""
    def post(self, request):
        """
        POST Create profile information to endpoint
        /api/profile/create/
        """
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Watch(APIView):
    permission_classes = [IsAuthenticated]
    """Watch Video Route"""
    def get(self, request, pk):
        """
        GET request to get all videos with the PROFILE
        rating using the profile's uuid endpoint is
        /api/watch/<str:pk>/
        """
        profile = Profile.objects.get(uuid=pk)
        agelimit = profile.age_limit
        movies = Movie.objects.get(age_limit=agelimit)
        showcase = MovieSerializer(movies)
        return Response(showcase.data)


class ShowMovieDetail(APIView):
    permission_classes = [IsAuthenticated]
    """Show Specific Movie Details"""
    def get(self, request, movie_id):
        """
        GET request to get the particular movies information through
        the movies uuid endpoint is /api/movie/detail/<str:movie_id>/
        """
        try:

            movie = Movie.objects.get(uuid=movie_id)
            serializer = MovieSerializer(movie)

            return Response(serializer.data)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class Search_Movie(APIView):
    permission_classes = [IsAuthenticated]
    """Search Movie Class"""
    def get(request, pk):
        """Search Movie Get request"""
        query = pk
        if query:
            movies = Movie.objects.filter(Q(title__icontains=query) |
                                          Q(description__icontains=query))
            serializer = MovieSerializer(movies, many=True)
            return Response(serializer.data)
        else:
            return Response({"movies": []})
