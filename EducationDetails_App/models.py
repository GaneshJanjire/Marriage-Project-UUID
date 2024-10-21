from django.db import models

# Create your models here.
from django.db import models
from UserProfile_app.models import UserProfile  # Assuming UserProfile model is in UserProfile_App

class EducationDetails(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    looking_for = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    occupation_details = models.CharField(max_length=255)
    annual_income = models.DecimalField(max_digits=10, decimal_places=2)
    employed_in = models.CharField(max_length=50)
    working_location = models.CharField(max_length=100)
    special_cases = models.CharField(max_length=255)

    def __str__(self):
        return f"Education Details for {self.user.name} {self.user.surname}"
