from django.urls import path
from . import views

urlpatterns = [
    path('authors', views.multiple_authors, name = 'authors'),
    path('authors/<int:pk>', views.single_author, name = 'author'),
    path('books', views.multiple_books, name='books'),
    path('books/<int:pk>', views.single_book, name='book'),
]