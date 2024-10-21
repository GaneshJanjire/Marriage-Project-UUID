from rest_framework import serializers
from .models import EducationDetails

class EducationDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationDetails
        fields = '__all__'
