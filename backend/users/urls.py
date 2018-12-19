from django.urls import path, include


urlpatterns = [
    path('api/auth/', include('rest_auth.urls')),
    path('api/register/', include('rest_auth.registration.urls')),
]