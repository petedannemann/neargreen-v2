from django.contrib.gis.geos import fromstr
from rest_framework import serializers

from .models import Store


class StoreSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)

    class Meta:
        model = Store
        fields = [
            'pk',
            'user',
            'name',
            'address',
            'location',
            'timestamp',
        ]
        read_only_fields = ['id', 'user']

    def to_representation(self, instance):
        ret = super(StoreSerializer, self).to_representation(instance)
        ret['distance'] = round(instance.distance.mi, 1)
        return ret

    def get_url(self, obj):
        request = self.context.get('request')
        return obj.get_api_url(request=request)