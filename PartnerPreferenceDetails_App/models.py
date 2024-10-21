from django.db import models

# Create your models here.
from django.db import models
from UserProfile_app.models import UserProfile

class PartnerPreferenceDetails(models.Model):
    CHOICE = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Transgender", "Transgender"),
    )
    
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    looking_for = models.CharField(max_length=20, choices=CHOICE)
    age_from = models.IntegerField()
    age_to = models.IntegerField()
    height_from = models.DecimalField(max_digits=4, decimal_places=2)
    height_to = models.DecimalField(max_digits=4, decimal_places=2)
    religion = models.CharField(max_length=50)
    caste = models.CharField(max_length=50)
    complexion = models.CharField(max_length=50)
    residency_status = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    education = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    partner_expectations = models.TextField()

    def __str__(self):
        return f"Partner Preferences for {self.user.name} {self.user.surname}"
