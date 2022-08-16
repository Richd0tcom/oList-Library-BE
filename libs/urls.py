from django.urls import path
from . import views

from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view


schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Library API",
        default_version='1.0.0',
        description="API documentation of the Olist library api",
    ),
    public=True,
)


urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-schema'),
    path('authors/', views.multiple_authors, name = 'authors'),
    path('authors/<int:pk>', views.single_author, name = 'author'),
    path('books/', views.multiple_books, name='books'),
    path('books/<int:pk>', views.single_book, name='book'),
]