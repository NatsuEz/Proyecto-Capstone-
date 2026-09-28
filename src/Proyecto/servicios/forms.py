from django import forms
from django.contrib.auth.models import User
from .models import PerfilCliente

class RegistroClienteForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=True, label="Nombre completo")
    email = forms.EmailField(required=True, label="Correo electrónico")
    password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")
    
    rut_empresa = forms.CharField(max_length=12, required=True, label="RUT Empresa / Persona")
    razon_social = forms.CharField(max_length=150, required=False, label="Razón Social")
    telefono = forms.CharField(max_length=20, required=False, label="Teléfono")

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            PerfilCliente.objects.create(
                user=user,
                rut_empresa=self.cleaned_data['rut_empresa'],
                razon_social=self.cleaned_data.get('razon_social', ''),
                telefono=self.cleaned_data.get('telefono', '')
            )
        return user