from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

class Message(models.Model):
    body = models.TextField(max_length=255, null=False)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    sender_id = models.PositiveIntegerField(null=False)
    content_sender = GenericForeignKey('content_type', 'sender_id')
    connection_id = models.ForeignKey('connections.Connection', null=False, on_delete=models.CASCADE, related_name='messages')
    created_at = models.DateTimeField(auto_now_add=True)

    def sender_type(self):
        return self.content_sender.__class__.__name__

    def connection_name(self):
        return str(self.connection_id.name)
