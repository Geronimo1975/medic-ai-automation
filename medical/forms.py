from django import forms
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from medical.models import Pacient
from .models import Pacient


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Utilizator", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Parolă", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
class PacientForm(forms.ModelForm):
     """
    Formularul PatientForm permite utilizatorului să introducă informații despre un pacient nou.

    Se bazează pe modelul Patient și include câmpuri pentru nume, prenume, vârstă și diagnostic.
    """
     class Meta:
        model = Pacient  # Verifică că modelul corespunde numelui corect din `models.py`
        fields = ['cod_formular', 'id', 'cod_pacient', 'nume', 'prenume', 'varsta', 'diagnostic']