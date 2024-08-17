from django.urls import path
from .views import calculate_view

urlspatterns = [
    path("calculate_view/<int:num>", calculate_view)
]