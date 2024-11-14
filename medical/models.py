from django.db import models
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Utilizator", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Parolă", widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class Pacient(models.Model):
    nume = models.CharField(max_length=100)
    prenume = models.CharField(max_length=100)
    varsta = models.IntegerField(default=0)  # sau orice valoare implicită care are sens pentru aplicația ta
    diagnostic = models.TextField()  # Asigură-te că acest câmp este definit

    def __str__(self):
        return f"{self.nume} {self.prenume}"
