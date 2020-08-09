from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from ..models import Puppy
from ..serializers import PuppySerializer


class ListPuppies(APITestCase):
    def setUp(self):
        Puppy.objects.create(
            name="Firulais", age=5, breed="Chilaquil", color="Morado"
        )
        Puppy.objects.create(
            name="Bosnia", age=5, breed="Chilaquil", color="Morado"
        )
        Puppy.objects.create(
            name="Clifford", age=5, breed="Gigante", color="Rojo"
        )

    def test_list_all_puppies_ok(self):
        response = self.client.get(reverse("puppies"))
        puppies = Puppy.objects.all()
        serializer = PuppySerializer(puppies, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_all_red_puppies(self):
        response = self.client.get(
            f"{reverse('puppies')}?color=Morado"
        )
        puppies = Puppy.objects.filter(color="Morado")
        serializer = PuppySerializer(puppies, many=True)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_not_found_puppies(self):
        response = self.client.get(
            f"{reverse('puppies')}?color=Rosa"
        )
        puppies = Puppy.objects.filter(color="Rosa")
        serializer = PuppySerializer(puppies, many=True)
        self.assertEqual(len(response.data), 0)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
