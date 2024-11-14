# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm
from django.shortcuts import render

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
