from django.urls import path
from .views import family_details

urlpatterns = [
    path('FamilyDetails/<uuid:uuid>/', family_details, name='family_details'),
]
