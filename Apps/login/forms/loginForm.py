from django import forms

class LoginForm(forms.Form):
    userRut = forms.CharField(label="Rut", max_length=10)
    password = forms.CharField(label="Contraseña")