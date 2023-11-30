from django import forms
from django.forms import ModelForm
from .models import fact_invitados, d_intolerancias, d_contacto, d_vegetariano


class NumAcompForm(forms.Form):

    num_adult = forms.IntegerField(label='Número de Adultos',
                                   widget=forms.NumberInput(attrs={'class': 'n_adults'}),
                                   initial=0)
    num_nin = forms.IntegerField(label='Número de Niños', widget=forms.NumberInput(attrs={'class': 'n_nin'}), initial=0)


class InvitadoForm(ModelForm):

    class Meta:
        model = fact_invitados
        fields = ['desc_nombre', 'id_vegetarian', 'id_intolerancias']
        labels = {
            'desc_nombre': 'Nombre y Apellidos',
            'id_vegetarian': '¿Vegetariano?',
            'id_intolerancias': '¿Intolerancias?'

        }
        widgets = {
            'desc_nombre': forms.TextInput(attrs={'class': 'lab-name'}),
            'id_vegetarian': forms.RadioSelect(attrs={'class': 'check-choice'})
        }


class IntoleranciasForm(ModelForm):

    class Meta:
        model = d_intolerancias
        fields = ['desc_intolerancias']
        labels = {
            'desc_intolerancias': '¿Intolerancias?'
        }
        widgets = {
            'desc_intolerancias': forms.SelectMultiple(attrs={'class': 'check-choice'})
        }


class VegetarianoForm(ModelForm):

    class Meta:
        model = d_vegetariano
        fields = ['flag_vegetarian']
        labels = {
            'flag_vegetarian': '¿Vegetariano?'
        }
        widgets = {
            'flag_vegetarian': forms.RadioSelect(attrs={'class': 'check-choice'}, choices=[('1', 'No'), ('2', 'Si')])
        }


class ContactConfForm(ModelForm):

    class Meta:
        model = d_contacto
        fields = ['nombre_contacto', 'desc_email', 'desc_telefono', 'id_intolerancias']
        labels = {
            'nombre_contacto': 'Nombre y Apellidos',
            'desc_email': 'Email',
            'desc_telefono': 'Teléfono',
            'id_intolerancias': '¿Intolerancias?'
        }
        widgets = {
            'nombre_contacto': forms.TextInput(attrs={'class': 'lab-name'}),
            'desc_email': forms.EmailInput(attrs={'class': 'lab-email'}),
            'desc_telefono': forms.TextInput(attrs={'class': 'lab-tlf'}),
        }
