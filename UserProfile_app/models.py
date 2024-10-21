from django.db import models
import uuid

class UserProfile(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    height = models.FloatField()
    blood_group = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.TextField()
    zipcode = models.CharField(max_length=10)
    profile_created_by = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=20)
    education = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    income = models.CharField(max_length=100)
    religion = models.CharField(max_length=50)   
    caste = models.CharField(max_length=50)
    subcaste = models.CharField(max_length=50)
    about_yourself = models.TextField()
    image = models.ImageField(upload_to='media/profile_images/')

    def __str__(self):
        return f"{self.name} {self.surname}"
