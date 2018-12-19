from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile

class ProfileCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Profile
        fields = ('username', 'email', 'image')

class ProfileChangeForm(UserChangeForm):

    class Meta:
        model = Profile
        fields = ('username', 'password', 'email', 'image')