import os
from django.core.wsgi import get_wsgi_application
from django.urls import path, include
from django.http import HttpResponse

# O funcție simplă pentru pagina de start
def home_view(request):
    return HttpResponse("Pagina de start a aplicației Medical AI")

urlpatterns = [
    path('medical/', include('medical.urls')),  # Ruta existentă pentru aplicația medical
    path('', home_view, name='home'),  # Noua rută pentru pagina de start
]



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medic_ai.settings')

application = get_wsgi_application()
