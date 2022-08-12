#these classes take python objects and turn them into JSON objects.

from rest_framework.serializers import ModelSerializer
from .models import Author, Book


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all'


class BookSerializer(ModelSerializer):
    authors = AuthorSerializer( many=True)
    class Meta:
        model = Book
        fields = '__all'

