from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Book, Author
import json

# Create your tests here.


class TestListBook(APITestCase):
    def setUp(self):
        self.sample_book = {
            "authors": [
                {
                    "name": "Osvaldo Santana Neto"
                }
            ],
            "name": "lib_book_x",
            "edition": 3,
            "publication_year": "2006"
        }

        # UPDATE BOOK
        self.new_bk = Book.objects.create(
            name="tst_bk", edition=3, publication_year="2005")
        self.new_bk.save()
        self.new_Author = Author.objects.create(name="boss")

        self.new_bk.authors.add(self.new_Author)

        self.sample_book2 = {
            "authors": [
                {
                    "name": "boss"
                }
            ],
            "name": "lib_book_x",
            "edition": 2,
            "publication_year": "2006"
        }

    def test_should_create_book(self):

        response = self.client.post(reverse("books"), data=json.dumps(
            self.sample_book), content_type='application/json')
        return self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_should_update_book(self):

        response = self.client.put(reverse("book", kwargs={'pk': self.new_bk.id}), data=json.dumps(
            self.sample_book2), content_type='application/json')
        return self.assertEqual(response.status_code, status.HTTP_200_OK)
