from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer

from .models import Profile


class UserSerializer(UserDetailsSerializer):
    image = serializers.ImageField(source="profile.image")

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('image',)

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        image = profile_data.get('image')

        instance = super(UserSerializer, self).update(instance, validated_data)

        # get and update user profile
        profile = instance.userprofile
        if profile_data and image:
            profile.image = image
            profile.save()
        return instance