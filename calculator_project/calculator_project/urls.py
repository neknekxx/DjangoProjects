# calculator_project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel URL
    path('', include('calculator.urls')),  # Include URLs from the calculator app
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # Serve static files in development
