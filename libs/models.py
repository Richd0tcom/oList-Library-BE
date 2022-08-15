from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=50)
    edition = models.IntegerField()
    publication_year = models.CharField(max_length=4)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.name