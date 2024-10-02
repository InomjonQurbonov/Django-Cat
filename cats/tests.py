from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from cats.models import Cats


class CatsAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        self.cat = Cats.objects.create(
            owner=self.user,
            cat_name="Fluffy",
            cat_age=3,
            cat_gender="Male",
            cat_breed="Siberian",
            cat_color="White",
            cat_details="Very fluffy and cute",
            cat_points=1
        )
        self.cat_url = reverse('кошка-list')

    def test_get_cats_list(self):
        response = self.client.get(self.cat_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['cat_name'], "Fluffy")

    def test_create_cat(self):
        data = {
            'owner': self.user.id,
            'cat_name': "Mittens",
            'cat_age': 2,
            'cat_gender': "Female",
            'cat_breed': "British Shorthair",
            'cat_color': "Grey",
            'cat_details': "Short and cute",
            'cat_points': 5
        }
        response = self.client.post(self.cat_url, data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cats.objects.count(), 2)
        self.assertEqual(Cats.objects.last().cat_name, "Mittens")
