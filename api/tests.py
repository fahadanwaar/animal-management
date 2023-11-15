from django.test import TestCase
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Animal
from .serializers import AnimalSerializer


class AnimalApiTests(TestCase):
    databases = {'default', 'memory'}
    def setUp(self):
        self.client = APIClient()

    def test_get_animal_list(self):
        url = reverse('animal-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_animal(self):
        url = reverse('animal-list')
        data = {'name': 'goat'}

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Animal.objects.using('memory').count(), 1)
        self.assertEqual(Animal.objects.using('memory').get().name, 'goat')

    def test_delete_animal(self):
        animal = Animal.objects.using('memory').create(name='markhor')
        url = reverse('animal-remove', args=[animal.id])

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Animal.objects.using('memory').count(), 0)
