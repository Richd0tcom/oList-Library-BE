from django_filters import FilterSet
from .models import Book

class BookFilter(FilterSet):

    class Meta:
        model = Book
        fields = {
            'name': ['exact', 'contains'],
            'edition': ['exact', 'contains'],
            'publication_year': ['exact', 'contains'],
            'authors': ['exact', 'contains'],   
        }