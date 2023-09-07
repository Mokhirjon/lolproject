from rest_framework import serializers
from .models import Genres,Authors,Books


class GenresSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields= ('name',)

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model : Books
        fields = ('name','image','price','pages','year','author','genre','desc')

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ('user', 'bio', 'date_of_birth', 'is_dead', 'date_of_dead', 'image', 'genre', 'country')