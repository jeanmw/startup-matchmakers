from rest_framework import serializers
from .models import Founder

class FounderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Founder
        fields = '__all__'
