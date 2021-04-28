from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from coolname import generate_slug
from faker import Faker

from tag.models import Tag
from place.models import Address


class PlaceTest(TestCase):
    fake = Faker()
    client = Client()

    def setUp(self):
        for i in range(5):
            Tag.objects.create(
                name=generate_slug(2)
            )
            Address.objects.create(
                address=self.fake.address()
            )

        self.valid_payload = {
            'name': 'Test place',
            'distance': '100',
            'address': '1',
            'tag': '1',
            'is_prefer': 'True',
        }

        self.invalid_payload = {
            'name': 'Test place',
            'distance': '100km',
            'address': '1',
            'tag': '1',
            'is_prefer': 'True',
        }

    def test_check_tags_count(self):
        self.assertEqual(Tag.objects.all().count(), 5)

    def test_check_addresses_count(self):
        self.assertEqual(Address.objects.all().count(), 5)

    def test_place_list_response_code(self):
        response = self.client.get(reverse('place_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_place(self):
        response = self.client.post(
            reverse('create_place'),
            data=self.valid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_place(self):
        response = self.client.post(
            reverse('create_place'),
            data=self.invalid_payload,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
