from django.test import TestCase

from ..models import Profile


class UserTest(TestCase):
    ''' Test module for User model '''

    def setUp(self):
        self.user = Profile.objects.create(
            username='TestUser',
            password='12345')

    def test_user_name(self):
        self.assertEqual(str(self.user), 'TestUser')

    def test_user_default_image(self):
        self.assertEqual(self.user.image, 'default.jpg')
        self.assertEqual(self.user.image.height, 228)
        self.assertEqual(self.user.image.width, 300) # Cropped to 300 based on Profile.save()