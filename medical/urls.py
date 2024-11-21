from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('chat/', views.chat_response, name='chat'),  # ruta pentru chat
    path('logout/', LogoutView.as_view(), name='logout'),  # ruta pentru logout
    path('login/', LoginView.as_view(), name='login'),  # ruta pentru login
    path('home/', views.home_view, name='home'),  # Exemplu de rută
    path('adauga-pacient/', views.add_patient, name='adauga_pacient'),  # Alt exemplu de rută
]








# from medical import views  # în views.py
# from django.urls import path, include
# from django.contrib.auth.views import LogoutView  # pentru LogoutView
# from django.contrib import admin
# from django.urls import path
# from . import views


# urlpatterns = [
#     path('chat/', views.chat_response, name='chat'),  # ruta pentru chat
#     path('logout/', LogoutView.as_view(), name='logout'),  # corectarea rutei logout
#     path('login/', views.login_view, name='login'),  # ruta pentru login
#     path('', include('medical.urls')),  # Aceasta va duce la o buclă recursivă
#     path('home/', views.home_view, name='home'),  # Exemplu de rută validă
#     path('adauga-pacient/', views.add_patient, name='adauga_pacient'),
#     path('admin/', admin.site.urls),
#     path('medical/', include('medical.urls')),  # Include rutele aplicației `medical`
# ]