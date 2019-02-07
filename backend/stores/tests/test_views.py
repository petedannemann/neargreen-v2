import json

from django.urls import reverse
from django.contrib.gis.geos import Point, fromstr
from django.contrib.gis.db.models.functions import Distance
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate
from rest_framework.authtoken.models import Token

from ..models import Store
from ..serializers import StoreSerializer
from ...users.models import Profile


class GetStoresTest(APITestCase):
    ''' Test module for GET stores API '''

    USERNAME = 'Neargreen'
    STORE_NAME = 'Mama Mia Pizzaria'
    ADDRESS = '1234 JFK Blvd'
    LONGITUDE = -75.1652
    LATITUDE = 39.9526
    SRID = 4326

    NUMBER_OF_STORES_IN_MIGRATION = 308

    def setUp(self):

        self.user = Profile.objects.get(username=self.USERNAME)

        self.store = Store.objects.create(
            user=self.user,
            name=self.STORE_NAME,
            address=self.ADDRESS,
            location = fromstr(f'POINT({self.LONGITUDE} {self.LATITUDE})', srid=self.SRID)
        )

        self.user_location = Point(self.LONGITUDE, self.LATITUDE, srid=self.SRID)

    # def test_get_stores(self):
    #     response = self.client.get(reverse('store-listcreate'))
    #     stores = Store.objects.all().annotate(
    #         distance=Distance('location', self.user_location)
    #     ).order_by('distance')[:25]
    #     serializer = StoreSerializer(stores)
    #     self.assertEqual(response.data['count'], self.NUMBER_OF_STORES_IN_MIGRATION)
    #     self.assertEqual(response.data['results'], serializer.data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_store(self):
        response = self.client.get(
            reverse('store-rud', kwargs={'pk': self.store.pk}),
            data={'longitude': self.LONGITUDE, 'latitude': self.LATITUDE}
        )
        store = Store.objects.annotate(
            distance=Distance('location', self.user_location)
        ).get(pk=self.store.pk)
        serializer = StoreSerializer(store)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_store(self):
        response = self.client.get(
            reverse('store-rud', kwargs={'pk': 99999999999999}),
            data={'longitude': self.LONGITUDE, 'latitude': self.LATITUDE}
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

# class CreateNewStoreTest(APITestCase):
#     ''' Test module for inserting a new store '''

#     USERNAME = 'Neargreen'
#     STORE_NAME = 'Mama Mia Pizzaria'
#     ADDRESS = '1234 JFK Blvd'
#     LONGITUDE = -75.1652
#     LATITUDE = 39.9526

#     def setUp(self):

#         self.user = Profile.objects.get(username=self.USERNAME)
#         self.token = Token.objects.get(user=self.user)
#         self.client.credentials(HTTP_AUTHORIZATION='JWT ' + self.token.key)

#         self.payload = {
#             'name': self.STORE_NAME,
#             'address': self.ADDRESS,
#             'location': {
#                 'type': 'Point',
#                 'coordinates': [
#                     self.LONGITUDE,
#                     self.LATITUDE
#                 ]
#             },
#         }

#     def test_create_store(self):
#         request = self.client.post(
#             reverse('store-listcreate'),
#             data=StoreSerializer(self.payload),
#             content_type='application/json'
#         )
#         self.assertEqual(request.status_code, status.HTTP_201_CREATED)

