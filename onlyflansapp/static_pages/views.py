from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Flan, ContactForm
from static_pages.forms import ContactFormForm


# Vista para la página de inicio
def index(request):
    """
    Renderiza la página de inicio con una lista de flanes públicos.
    """
    flans = Flan.objects.filter(is_private=False)
    return render(request, "index.html", {"flans": flans})


# Vista para la página "Acerca de"
def about(request):
    """
    Renderiza la página "Acerca de".
    """
    return render(request, "about.html", {})


# Vista para la página de bienvenida
def welcome(request):
    """
    Renderiza la página de bienvenida con una lista de flanes privados.
    """
    flans = Flan.objects.filter(is_private=True)
    return render(request, "welcome.html", {"flans": flans})


# Vista para el formulario de contacto
def contact(request):
    """
    Renderiza el formulario de contacto y maneja los datos enviados.
    Si se envía un formulario válido, crea un objeto ContactForm y redirige a la página de éxito.
    """
    if request.method == "POST":
        form = ContactFormForm(request.POST)
        if form.is_valid():
            # Crea un nuevo objeto ContactForm con los datos del formulario
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            # Redirige a la página de éxito después de enviar el formulario
            return HttpResponseRedirect("/exito")
    else:
        # Muestra un formulario vacío si la solicitud es GET
        form = ContactFormForm()

    return render(request, "contact.html", {"form": form})
