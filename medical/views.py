from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from medical.forms import LoginForm
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from medical.models import Pacient
from .forms import PacientForm # relative import
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from medical.models import Pacient
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Pacient
from django.http import JsonResponse
from transformers import pipeline

# Inițializare pipeline NLP (conversational model)
chatbot_pipeline = pipeline("conversational", model="microsoft/DialoGPT-small")

def chat_response(request):
    if request.method == "POST":
        user_input = request.POST.get("message")
        if user_input:
            # Generează un răspuns folosind modelul NLP
            conversation = chatbot_pipeline(user_input)
            response_text = conversation.generated_responses[-1]  # Ultimul răspuns generat
            return JsonResponse({"response": response_text})
    return JsonResponse({"error": "Invalid request"}, status=400)


def add_patient(request):
    """
    Permite utilizatorului să adauge un pacient nou în baza de date.

    - Dacă metoda de cerere este POST, formularul de pacient este validat și salvat în baza de date.
    - Dacă metoda de cerere este GET, este afișat un formular gol pentru adăugarea unui pacient nou.

    Args:
        request (HttpRequest): Obiectul de cerere HTTP care conține datele trimise de utilizator.

    Returns:
        HttpResponse: Pagina HTML fie cu un formular gol, fie cu erori de validare sau redirecționează
        utilizatorul la lista de pacienți după salvare.
    """
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'medical/adauga_pacient.html', {'form': form})

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'medical/lista_pacienti.html', {'patients': patients})


@login_required # Decorator pentru a asigura că utilizatorul este autentificat
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'medical/lista_pacienti.html', {'patients': patients})




chatbot_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2", framework="tf")

def chat_response(request):
    user_message = request.GET.get("message", "")
    response = chatbot_pipeline({
        'question': user_message,
        'context': "Informații medicale generale..."  # Adaugă un context relevant
    })
    return JsonResponse({"response": response['answer']})

@login_required
def lista_pacienti(request):
    pacienti = Pacient.objects.all()
    return render(request, 'medical/lista_pacienti.html', {'pacienti': pacienti})

@login_required
def editeaza_pacient(request, pacient_id):
    pacient = get_object_or_404(Pacient, id=pacient_id)
    if request.method == 'POST':
        form = PacientForm(request.POST, instance=pacient)
        if form.is_valid():
            form.save()
            return redirect('lista_pacienti')
    else:
        form = PacientForm(instance=pacient)
    return render(request, 'medical/editeaza_pacient.html', {'form': form})


def adauga_pacient(request):
    return render(request, 'medical/adauga_pacient.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Bine ai venit, {username}!")
                return redirect('home')  # redirecționează la pagina principală după logare
            else:
                messages.error(request, "Utilizator sau parolă incorectă.")
        else:
            messages.error(request, "Formular invalid.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def home_view(request):
    return render(request, 'medical/home.html')