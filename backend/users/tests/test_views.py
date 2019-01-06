from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Profile


# class JwtVerifyTest(APITestCase):

#     USERNAME = 'TestUser'
#     PASSWORD = '12345'

#     def setUp(self):
#         self.user = Profile.objects.create(
#             username=self.USERNAME,
#             password=self.PASSWORD
#         )
#         self.valid_payload = {
#             'username': self.USERNAME,
#             'password': self.PASSWORD
#         }

#     def test_valid_login(self):
#         response = self.client.post('api/auth/login', self.valid_payload, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
    