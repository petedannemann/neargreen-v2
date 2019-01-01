from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.gis.geos import fromstr

from ..models import Store
from ...users.models import Profile


class StoreTest(TestCase):
    ''' Test module for Store model '''

    def setUp(self):
        longitude = -75.1652
        latitude = 39.9526

        # Made by stores/migrations/0003
        user = Profile.objects.get(username='Neargreen')

        Store.objects.create(
            user=user,
            name='Mama Mia Pizzaria',
            address='1234 JFK Blvd',
            location = fromstr(f'POINT({longitude} {latitude})', srid=4326)
        )

    def test_store_name(self):
        store_pizzaria = Store.objects.get(name='Mama Mia Pizzaria')
        self.assertEqual(str(store_pizzaria), 'Mama Mia Pizzaria')

    def test_store_owner(self):
        store_pizzaria = Store.objects.get(name='Mama Mia Pizzaria')
        user = Profile.objects.get(username='Neargreen')
        self.assertEqual(store_pizzaria.owner, user)

    def test_store_api_url(self):
        store_pizzaria = Store.objects.get(name='Mama Mia Pizzaria')
        store_pizzaria_api_url = f'/api/stores/{store_pizzaria.pk}/'
        self.assertEqual(store_pizzaria.get_api_url(), store_pizzaria_api_url)
