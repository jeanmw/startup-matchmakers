from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = (
            'id',
            'body',
            'content_type',
            'sender_id',
            'sender_type',
            'sender_name',
            'connection_id',
            'connection_name',
            'created_at'
            )
