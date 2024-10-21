from django.urls import path
from .views import habbits_interest_details

urlpatterns = [
    path('Habbit_Interests/<uuid:uuid>/', habbits_interest_details, name='habbits_interest_details'),
]
