from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # Add a sample route if needed
]
