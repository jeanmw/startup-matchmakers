from django.shortcuts import render
from .models import Connection
from .serializers import ConnectionSerializer
from rest_framework import generics

class ConnectionListCreate(generics.ListCreateAPIView):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer
