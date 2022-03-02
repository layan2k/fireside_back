from django.urls import path

from fireside_api.views import MovieList

urlpatterns = [
    path('video/', MovieList.as_view()),
]
