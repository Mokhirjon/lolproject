from django.urls import path
from .views import ListGenresApiew,ListBookbyAthorApiew
urlpatterns = [
    path ('all_genres/',ListGenresApiew.as_view()),
    path('book_by_author',ListBookbyAthorApiew.as_view())
]