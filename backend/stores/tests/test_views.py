import json

from django.urls import reverse
from django.contrib.gis.geos import Point, fromstr
from django.contrib.gis.db.models.functions import Distance
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Store
from ..serializers import StoreSerializer
from ...users.models import Profile
from ...users.serializers import UserSerializer


class GetStoresTest(APITestCase):
    ''' Test module for GET stores API '''

    def setUp(self):
        longitude = -75.1652
        latitude = 39.9526

        user = Profile.objects.get(username='Neargreen')

        self.chineseFood = Store.objects.create(
            user=user,
            name='Chinese Food',
            address='1234 JFK Blvd',
            location = fromstr(f'POINT({longitude} {latitude})', srid=4326)
        )

        self.user_location = Point(longitude, latitude, srid=4326)

    # def test_get_stores(self):
    #     ' Pretty tricky due to pagination... Gotta come back to this one'
    #     response = client.get(reverse('store-listcreate'))
    #     stores = Store.objects.annotate(
    #         distance=Distance('location', self.user_location)
    #     ).order_by('distance')[:25]
    #     serializer = StoreSerializer(stores, many=True)
    #     self.assertEqual(response.data, serializer.data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_store(self):
        response = self.client.get(reverse('store-rud', kwargs={'pk': self.chineseFood.pk}))
        chineseFood = Store.objects.annotate(
            distance=Distance('location', self.user_location)
        ).get(pk=self.chineseFood.pk)
        serializer = StoreSerializer(chineseFood)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_store(self):
        response = self.client.get(reverse('store-rud', kwargs={'pk': 99999999999999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewStoreTest(APITestCase):
    ''' Test module for inserting a new store '''

    def setUp(self):
        longitude = -75.1652
        latitude = 39.9526

        user = Profile.objects.get(username='Neargreen')

        self.valid_payload = {
            'name': 'Generic Name',
            'address': '1234 JFK Blvd',
            'location': {
                'type': 'Point',
                'coordinates': [
                    longitude,
                    latitude
                ]
            },
        }
        self.invalid_payload = {
            'name': 'Generic Name',
            'address': '1234 JFK Blvd',
            'location': {
                'type': 'Point',
                'coordinates': [
                    longitude,
                    latitude
                ]
            },
        }

    # def test_create_valid_store(self):
    #    'Need to test auth before doing this'
    #     response = client.post(
    #         reverse('store-listcreate'),
    #         data=json.dumps(self.valid_payload),
    #         content_type='application/json'
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

