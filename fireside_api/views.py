from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from fireside_api.models import Movie
from fireside_api.serializer import MovieSerializer, ProfileSerializer
from .models import Profile, Movie
# Create your views here.

class MovieList(APIView):
    def get(self, request):
        movie= Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)
        return Response(serializer.data)

class ProfileList(APIView):

    def get(self, request):
        profiles=Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

class ProfileCreate(APIView):

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Watch(APIView):
    def get(self, request, pk):
            profile=Profile.objects.get(uuid=pk)
            agelimit = profile.age_limit
            movies=Movie.objects.get(age_limit=agelimit)
            showcase= MovieSerializer(movies)


            return Response(showcase.data)



class ShowMovieDetail(APIView):
    def get(self,request,movie_id,*args, **kwargs):
        try:

            movie=Movie.objects.get(uuid=movie_id)
            serializer = MovieSerializer(movie)

            return Response(serializer.data)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ShowMovie(APIView):
    def get(self,request,movie_id):
        try:

            movies=Movie.objects.get(uuid=movie_id)

            serializer = MovieSerializer(movies)


            return Response(serializer.data)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

