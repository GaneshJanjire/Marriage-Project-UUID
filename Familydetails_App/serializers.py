from rest_framework import serializers
from .models import FamilyDetails

class FamilyDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyDetails
        fields = '__all__'
