from django.db import models

# Create your models here.
from django.db import models
from UserProfile_app.models import UserProfile  # Assuming UserProfile model is in UserProfile_App

class ContactUs(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=15)
    alternative_mobile_number = models.CharField(max_length=15, blank=True, null=True)
    convenient_time_to_call = models.CharField(max_length=50)
    email = models.EmailField()
    permanent_address = models.TextField()
    working_address = models.TextField()

    def __str__(self):
        return f"Contact Information for {self.user.name} {self.user.surname}"
