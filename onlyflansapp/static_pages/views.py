from django.shortcuts import render
from .models import Flan


# Create your views here.
def index(request):
    flans = Flan.objects.filter(is_private=False)
    return render(request, "index.html", {"flans": flans})


def about(request):
    return render(request, "about.html", {})


def welcome(request):
    flans = Flan.objects.filter(is_private=True)
    return render(request, "welcome.html", {"flans": flans})
