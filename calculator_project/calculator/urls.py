# calculator/urls.py

from django.urls import path
from . import views  # Import views from the same directory

urlpatterns = [
    path('', views.home, name='home'),  # Map the root URL of the app to the home view
]
