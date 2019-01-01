from django.db.models import Q
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from rest_framework import generics, mixins
from rest_framework.settings import api_settings

from .models import Store
from .permissions import IsOwnerOrReadOnly
from .serializers import StoreSerializer


longitude = -75.1652
latitude = 39.9526

user_location = Point(longitude, latitude, srid=4326)

class StoreAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = StoreSerializer
    permission_classes = [IsOwnerOrReadOnly]
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS

    def get_queryset(self):
        queryset = Store.objects.annotate(
            distance=Distance('location', user_location)
        ).order_by('distance')
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}

class StoreRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = StoreSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Store.objects.annotate(
            distance=Distance('location', user_location)
        )

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}

