from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

# Create your tests here.


class TestListBook(APITestCase):

    def test_should_create_book(self):
        sample_book = {
            "authors": [
                {
                    "name": "Osvaldo Santana Neto"
                }
            ],
            "name": "lib_book_x",
            "edition": 3,
            "publication_year": "2006"
        }
        response = self.client.post(reverse("books"), sample_book)
        return self.assertEqual(response.status_code, status.HTTP_201_CREATED)
