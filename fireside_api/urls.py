"""url paths for the fireside_api"""
from django.urls import path

from fireside_api.views import MovieList, ProfileList, ProfileCreate, Search_Movie
from fireside_api.views import Watch, ShowMovieDetail

urlpatterns = [
    path('video/', MovieList.as_view()),
    path('profile/', ProfileList.as_view(), name='profile_list'),
    path('profile/create/', ProfileCreate.as_view(), name='profile_create'),
    path('watch/<str:pk>/', Watch.as_view(), name='watch'),
    path('movie/detail/<str:movie_id>/', ShowMovieDetail.as_view(),
         name='show_det'),
    path('movie/search/<str:pk>/', Search_Movie.as_view, name='search'),
]
