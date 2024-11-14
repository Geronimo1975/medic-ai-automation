from django.urls import path
from medical import views as medical_views
from django.http import HttpResponse

def home(request):
    return HttpResponse("Pagina principală a aplicației medical")
