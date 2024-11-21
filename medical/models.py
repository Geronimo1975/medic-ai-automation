from django.db import models
from django import forms
from django.contrib.auth.forms import AuthenticationForm



class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Utilizator", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Parolă", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

"""
    Modelul Patient reprezintă un pacient în baza de date a aplicației medicale.
    
    Atribute:
        nume (CharField): Numele pacientului.
        prenume (CharField): Prenumele pacientului.
        varsta (IntegerField): Vârsta pacientului.
        diagnostic (TextField): Diagnostic sau observații legate de pacient.
    """

class Pacient(models.Model):
    nume = models.CharField(max_length=100)
    prenume = models.CharField(max_length=100)
    varsta = models.IntegerField(default=0)
    diagnostic = models.TextField()
    cod_formular = models.CharField(max_length=100)
    cod_pacient = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    
def __str__(self):
    """
    Returnează reprezentarea text a obiectului Patient, utilizând numele și prenumele.
    """
    return f"{self.nume} {self.prenume}"

