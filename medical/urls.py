from django.urls import path
from . import views  # importă views dacă ai definit vreun view

urlpatterns = [
    path('', views.home, name='home'),  # exemplu de rută pentru view-ul home din views.py
]
