from rest_framework import serializers
from .models import Habbits_Interest

class HabbitsInterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habbits_Interest
        fields = '__all__'
