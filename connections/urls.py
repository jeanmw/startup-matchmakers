from django.urls import path
from . import views

urlpatterns = [
    path('api/connection/', views.ConnectionListCreate.as_view() ),
]
