from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group

from .forms import ProfileCreationForm, ProfileChangeForm
from .models import Profile


class ProfileAdmin(UserAdmin):
    add_form = ProfileCreationForm
    form = ProfileChangeForm
    model = Profile
    list_display = ['email', 'username', 'image']

admin.site.register(Profile, ProfileAdmin)
admin.site.unregister(Site)
admin.site.unregister(Group)
