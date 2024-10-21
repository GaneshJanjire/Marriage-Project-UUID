from django.db import models

# Create your models here.
from django.db import models
from UserProfile_app.models import UserProfile  # Assuming UserProfile model is in UserProfile_App

class HoroscopeDetails(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    moon_sign = models.CharField(max_length=50)
    star = models.CharField(max_length=50)
    gotra = models.CharField(max_length=50)
    manglik = models.BooleanField()
    shani = models.BooleanField()
    horoscope_match = models.BooleanField()
    place_of_birth = models.CharField(max_length=100)
    place_of_country = models.CharField(max_length=100)
    hours = models.PositiveIntegerField()
    minutes = models.PositiveIntegerField()
    seconds = models.PositiveIntegerField()
    am_pm = models.CharField(max_length=2)

    def __str__(self):
        return f"Horoscope Details for {self.user.name} {self.user.surname}"
