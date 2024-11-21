from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from .views import NERView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("medical/", include("medical.urls")),
    path("", views.home_view, name="home"),
    path("chat/", views.chat_response, name="chat_response"),  # Ruta pentru chatbot
    path("classify/", views.classify_view, name="classify"),
    path("ner/", views.ner_view, name="ner"),
    path('', include('medical.urls')),  # Asigură-te că aplicația ta este inclusă corect
    path('ner/', NERView.as_view(), name='ner'),
]
