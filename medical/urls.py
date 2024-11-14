# medical/urls.py
from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('medical/', include('medical.urls')),  # include toate rutele din aplicația `medical`
    # alte rute globale...
]

urlpatterns = [
    path('adauga-pacient/', views.adauga_pacient, name='adauga_pacient'),
    # alte rute...
]
