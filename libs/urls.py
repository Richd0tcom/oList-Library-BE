from django.urls import path
from . import views

urlpatterns = [
    path('', views.getAuthors, name = 'Authors'),
]