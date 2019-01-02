from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.gis.geos import fromstr

from ..models import Store
from ...users.models import Profile


class StoreTest(TestCase):
    ''' Test module for Store model '''

    USERNAME = 'Neargreen'
    STORE_NAME = 'Mama Mia Pizzaria'
    ADDRESS = '1234 JFK Blvd'
    LONGITUDE = -75.1652
    LATITUDE = 39.9526

    def setUp(self):
        # Made by stores/migrations/0003
        self.user = Profile.objects.get(username=self.USERNAME)

        self.store = Store.objects.create(
            user=self.user,
            name=self.STORE_NAME,
            address=self.ADDRESS,
            location = fromstr(f'POINT({self.LONGITUDE} {self.LATITUDE})', srid=4326)
        )

    def test_store_name(self):
        self.assertEqual(str(self.store), self.STORE_NAME)

    def test_store_owner(self):
        self.assertEqual(self.store.owner, self.user)

    def test_store_api_url(self):
        store_api_url = f'/api/stores/{self.store.pk}/'
        self.assertEqual(self.store.get_api_url(), store_api_url)
