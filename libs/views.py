from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# Create your views here.

@api_view('GET', 'POST')
def multiple_authors(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    print(serializer)
    return Response(serializer.data)


@api_view('GET', 'POST')
def single_author(request, pk):
    if request.method == 'GET':
        author = Author.objects.get(id=pk)
        serializer1 = AuthorSerializer(author, many=False)

        return Response(serializer1.data)
        
        

    elif request.method == 'POST':
        serializer2 = AuthorSerializer(data=request.data)
        if serializer2.is_valid():
            serializer2.save()
            return Response(serializer2.data, status=status.HTTP_201_CREATED)




@api_view('GET')
def multiple_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books)
    
    return Response(serializer.data)


@api_view('GET', 'POST')
def single_book(request, pk):

    try:
        #modify this to include filters
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        author = Book.objects.get(id=pk)
        serializer1 = BookSerializer(author, many=False)

        return Response(serializer1.data)
        
        

    elif request.method == 'POST':
        serializer2 = BookSerializer(data=request.data)
        if serializer2.is_valid():
            serializer2.save()
            return Response(serializer2.data, status=status.HTTP_201_CREATED)
    
    elif request.method == 'PUT':
        serializer3 = BookSerializer(data=request.data)
        if serializer3.is_valid():
            serializer3.save()
            return Response(serializer2.data, status=status.HTTP_201_CREATED)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        


