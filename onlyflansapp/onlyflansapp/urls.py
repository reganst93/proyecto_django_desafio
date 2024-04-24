"""
URL configuration for onlyflansapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# urls.py

from django.contrib import admin
from django.urls import path, include
from static_pages.views import index, about, welcome, contact, register

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="indice"),
    path("about/", about, name="acerca"),
    path("welcome/", welcome, name="bienvenidos"),
    path("contact/", contact, name="contacto"),
    path("accounts/", include("django.contrib.auth.urls")),  # URLs de autenticación
    path("register/", register, name="registro"),
]
