from django.urls import path
from .views import get_crypto_data

urlpatterns = [
    path('get-crypto-data/', get_crypto_data, name='get_crypto_data'),
]