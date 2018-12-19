from django.urls import path

from .views import PostRudView, PostAPIView


urlpatterns = [
    path('api/posts/', PostAPIView.as_view(), name='post-listcreate'),
    path('api/posts/<int:pk>/', PostRudView.as_view(), name='post-rud'),
]