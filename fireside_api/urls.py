"""url paths for the fireside_api"""
from django.urls import path

from fireside_api import views

urlpatterns = [
    path('video/', views.MovieList.as_view()),
    path('profile/', views.ProfileList.as_view(), name='profile_list'),
    path('profile/create/', views.ProfileCreate.as_view(), name='profile_create'),
    path('watch/<str:pk>/', views.Watch.as_view(), name='watch'),
    path('movie/detail/<str:movie_id>/', views.ShowMovieDetail.as_view(),
         name='show_det'),
    path('movie/play/<str:movie_id>/', views.ShowMovie.as_view(), name='play'),
    path('movie/search/<str:pk>/', views.search_movie, name='search'),
]
