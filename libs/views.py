from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from .filters import BookFilter

# Create your views here.


@api_view(['GET', 'POST'])
def multiple_authors(request):
    paginator = PageNumberPagination()
    paginator.page_size = 5

    authors = Author.objects.all()

    queryS = paginator.paginate_queryset(authors, request)

    serializer = AuthorSerializer(queryS, many=True)
    print(serializer)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
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


@api_view(['GET', 'POST'])
def multiple_books(request):
    if request.method == 'GET':

        books = Book.objects.all()

        book_filter = BookFilter(request.GET, queryset=books)
        if book_filter.is_valid():
            queryS = book_filter.qs

        serializer = BookSerializer(queryS, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':

        serializer2 = BookSerializer(data=request.data)
        if serializer2.is_valid():
            serializer2.save()
            return Response(serializer2.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer2.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def single_book(request, pk):

    try:
        # modify this to include filters
        book = Book.objects.get(id=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer1 = BookSerializer(book, many=False)
        return Response(serializer1.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer3 = BookSerializer(book, data=request.data)
        if serializer3.is_valid():
            serializer3.save()
            return Response(data=serializer3.data, status=status.HTTP_200_OK)

        return Response(data=serializer3.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
