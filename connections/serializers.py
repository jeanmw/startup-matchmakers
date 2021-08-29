from rest_framework import serializers
from .models import Connection
from messaging.serializers import MessageSerializer

class ConnectionSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)
    class Meta:
        model = Connection
        fields = '__all__'
        read_only_fields = ['name', 'messages']
