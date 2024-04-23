from django import forms
from django.contrib.auth.forms import UserCreationForm


class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(label="Correo")
    customer_name = forms.CharField(max_length=64, label="Nombre")
    messages = forms.CharField(label="Mensaje")


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = (
            "username",
            "email",
        )  # Lista de campos que se mostrarán en el formulario
