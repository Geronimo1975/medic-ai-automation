from django import forms
from .models import Pacient
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Utilizator", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Parolă", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
class PacientForm(forms.ModelForm):
    class Meta:
        model = Pacient
        fields = ['nume', 'prenume', 'varsta', 'diagnostic']
