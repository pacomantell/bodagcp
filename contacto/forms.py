from django.forms import ModelForm
from django import forms

from .models import MensajeContacto


class ContactForm(ModelForm):

    class Meta:
        model = MensajeContacto
        fields = ['desc_nombre', 'email', 'desc_mensaje']
        labels = {
            'desc_nombre': 'Nombre y Apellidos',
            'email': 'Email',
            'desc_mensaje': 'Mensaje'
        }
        widgets = {
            'desc_nombre': forms.TextInput(attrs={'class': 'lab-name'}),
            'email': forms.EmailInput(attrs={'class': 'lab-email'})
        }
