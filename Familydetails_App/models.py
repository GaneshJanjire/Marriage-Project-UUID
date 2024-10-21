from django.db import models

# Create your models here.
from django.db import models
from UserProfile_app.models import UserProfile

class FamilyDetails(models.Model):
    CHOICE = (
        ('My parents will stay with me after marriage', 'My parents will stay with me after marriage'),
        ('My parents will not stay with me after marriage', 'My parents will not stay with me after marriage'),
        ('Dont wish to specify', 'Dont wish to specify'),
    )
    
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    looking_for = models.CharField(max_length=50, choices=CHOICE)
    family_values = models.CharField(max_length=100)
    family_type = models.CharField(max_length=100)
    family_status = models.CharField(max_length=100)
    no_of_brothers = models.IntegerField()
    no_of_brothers_married = models.IntegerField()
    no_of_sisters = models.IntegerField()
    no_of_sisters_married = models.IntegerField()
    mother_tongue = models.CharField(max_length=50)
    father_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100)
    family_wealth = models.CharField(max_length=100)
    about_family = models.TextField()

    def __str__(self):
        return f"Family Details for {self.user.name} {self.user.surname}"
