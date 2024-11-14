from django.contrib import admin
from django.urls import path, include
from medical import views as medical_views


urlpatterns = [
    path('', medical_views.home, name='home'),  # referința corectă la view-ul 'home'
    path('admin/', admin.site.urls),
    path('medical/', include('medical.urls')),
    # adaugă aici restul rutelor necesare
]