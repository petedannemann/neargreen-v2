from django.contrib.gis.db import models
from django.conf import settings
from rest_framework.reverse import reverse as api_reverse


class Store(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, null=True, blank=True)
    address = models.TextField(max_length=120, null=True, blank=True)
    location = models.PointField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def owner(self):
        return self.user

    def get_api_url(self, request=None):
        return api_reverse('store-rud', kwargs={'pk': self.pk}, request=request)
