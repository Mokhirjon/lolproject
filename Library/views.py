from  django.shortcuts import render
from rest_framework import generics
from .models import Authors,Books,Genres
from .serializers import GenresSerializers,BooksSerializer,AuthorSerializer
from config.permissions import AdminPermission,AuthorPermission
# Create your views here.
class ListGenresApiew(generics.ListCreateAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializers
    permission_classes = (AdminPermission,)


class ListBookbyAthorApiew(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = (AuthorPermission,)

    def get_queryset(self):
        user =self.request.user
        author=Authors.objects.get(user=user)
        return Books.objects.filter(author=author.id)