#these classes take python objects and turn them into JSON objects.

from rest_framework.serializers import ModelSerializer
from .models import Author, Book


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(ModelSerializer):
    authors = AuthorSerializer( many=True)
    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        authr = validated_data.pop('authors')
        bk = Book.objects.create(**validated_data)
        

        for athr in authr:
           a = Author.objects.create(name=athr["name"])
           a.save()
           bk.authors.add(a)
           
        return bk


