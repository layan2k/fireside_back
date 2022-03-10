from django.urls import path

from fireside_api.views import MovieList, ProfileList, ProfileCreate, Test ,Watch,ShowMovieDetail,ShowMovie

urlpatterns = [
    path('video/', MovieList.as_view()),
    path('profile/',ProfileList.as_view(),name='profile_list'),
    path('profile/create/',ProfileCreate.as_view(),name='profile_create'),
    path('watch/<str:pk>/',Watch.as_view(),name='watch'),
    path('movie/detail/<str:movie_id>/',ShowMovieDetail.as_view(),name='show_det'),
    path('movie/play/<str:movie_id>/',ShowMovie.as_view(),name='play'),
    path('test/',Test.as_view(),name='test')
]
