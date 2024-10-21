from rest_framework import serializers
from .models import PartnerPreferenceDetails

class PartnerPreferenceDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerPreferenceDetails
        fields = '__all__'
