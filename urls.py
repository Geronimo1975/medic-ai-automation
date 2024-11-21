# proiect/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('medical_ai/', include('medical_ai.urls')),  # Include URL-urile aplicației medical_ai
]
