from django.shortcuts import render
from .models import Founder
from .serializers import FounderSerializer
from rest_framework import generics

class FounderListCreate(generics.ListCreateAPIView):
    queryset = Founder.objects.all()
    serializer_class = FounderSerializer
