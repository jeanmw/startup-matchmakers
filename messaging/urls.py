from django.urls import path
from . import views

urlpatterns = [
    path('api/message/', views.MessageListCreate.as_view() ),
]
