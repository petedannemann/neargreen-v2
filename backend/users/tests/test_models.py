from django.test import TestCase

from ..models import Profile


class UserTest(TestCase):
    ''' Test module for User model '''

    USERNAME = 'TestUser'
    PASSWORD = '12345'

    DEFAULT_IMAGE = 'default.jpg'
    DEFAULT_IMAGE_HEIGHT = 228
    IMAGE_MAX_SIZE = 300

    def setUp(self):
        self.user = Profile.objects.create(
            username=self.USERNAME,
            password=self.PASSWORD)

    def test_user_name(self):
        self.assertEqual(str(self.user), self.USERNAME)

    def test_user_default_image(self):
        self.assertEqual(self.user.image, self.DEFAULT_IMAGE)
        self.assertEqual(self.user.image.height, self.DEFAULT_IMAGE_HEIGHT)
        self.assertEqual(self.user.image.width, self.IMAGE_MAX_SIZE) # Cropped to 300 based on Profile.save()