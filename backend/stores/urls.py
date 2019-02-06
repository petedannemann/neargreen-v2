from django.urls import path

from .views import StoreAPIView, StoreRudView


urlpatterns = [
    path('api/stores/', StoreAPIView.as_view(), name='store-listcreate'),
    path('api/stores/<int:pk>/', StoreRudView.as_view(), name='store-rud'),
]