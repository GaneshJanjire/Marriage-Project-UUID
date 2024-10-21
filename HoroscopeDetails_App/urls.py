from django.urls import path
from .views import horoscope_details

urlpatterns = [
    path('HoroscopeDetail/<uuid:uuid>/', horoscope_details, name='horoscope_details'),  # Single endpoint for all methods
]
