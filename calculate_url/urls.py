from django.urls import path
from .views import calculate_view

urlspatterns = [
    path("calculate/<int:num>", calculate_view)
]