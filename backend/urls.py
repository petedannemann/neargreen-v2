from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

from .stores.views import StoreAPIView, StoreRudView


urlpatterns = [
    path('api/auth/', obtain_jwt_token, name='api-login'),
    path('', include('backend.users.urls')),
    path('', include('backend.stores.urls')),
    path('admin/', admin.site.urls),
]
