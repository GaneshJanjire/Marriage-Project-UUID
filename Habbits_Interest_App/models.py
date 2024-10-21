from django.db import models

# Create your models here.
from django.db import models
from UserProfile_app.models import UserProfile

class Habbits_Interest(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    sports = models.CharField(max_length=100)
    movie = models.CharField(max_length=100)
    books = models.CharField(max_length=100)
    travel = models.CharField(max_length=100)
    volunteer_work = models.CharField(max_length=100)
    cooking = models.CharField(max_length=100)
    music = models.CharField(max_length=100)
    writing = models.CharField(max_length=100)
    gaming = models.CharField(max_length=100)
    gardening = models.CharField(max_length=100)

    def __str__(self):
        return f"Habbits and Interests for {self.user.name} {self.user.surname}"
