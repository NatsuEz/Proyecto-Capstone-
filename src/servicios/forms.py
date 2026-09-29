from django import forms
from .models import Cliente, Contratacion

class RegistroClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'tipo_persona',
            'rut',
            'razon_social',
            'nombre_fantasia',
            'giro',
            'email',
            'telefono',
            'direccion',
            'comuna',
            'region',
            'rep_legal_nombre',
            'rep_legal_rut',
            'rep_legal_email',
        ]
        widgets = {
            'tipo_persona': forms.Select(attrs={'class': 'form-select'}),
            'rut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 76.123.456-7'}),
            'razon_social': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre o Razón Social'}),
            'nombre_fantasia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de Fantasía'}),
            'giro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Giro comercial'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@empresa.cl'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+56 9 1234 5678'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Calle, número, oficina'}),
            'comuna': forms.TextInput(attrs={'class': 'form-control'}),
            'region': forms.TextInput(attrs={'class': 'form-control'}),
            'rep_legal_nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'rep_legal_rut': forms.TextInput(attrs={'class': 'form-control'}),
            'rep_legal_email': forms.EmailInput(attrs={'class': 'form-control'}),
        }