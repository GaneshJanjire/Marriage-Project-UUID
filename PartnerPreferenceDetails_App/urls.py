from django.urls import path
from .views import partner_preference_details

urlpatterns = [
    path('PartnerPreference/<uuid:uuid>/', partner_preference_details, name='partner_preference_details'),
]
