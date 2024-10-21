from django.urls import path
from .views import education_details

urlpatterns = [
    path('EducationDetails/<uuid:uuid>/', education_details, name='education_details'),  # Single endpoint for all methods
]
