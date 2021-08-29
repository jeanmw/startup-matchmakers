from django.shortcuts import render
from .models import Investor
from .serializers import InvestorSerializer
from rest_framework import generics

class InvestorListCreate(generics.ListCreateAPIView):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer
