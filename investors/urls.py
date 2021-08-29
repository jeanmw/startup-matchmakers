from django.urls import path
from . import views

urlpatterns = [
    path('api/investor/', views.InvestorListCreate.as_view() ),
]
