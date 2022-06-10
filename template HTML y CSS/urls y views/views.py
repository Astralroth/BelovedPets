from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

def redirect_to_root (request):
    return HttpResponseRedirect('login')

def index(request):
    return render(request, 'core/index.html')

def login(request):
    return render(request, 'core/cred/login.html')

def Administrar(request):
    return render(request, 'core/administrar.html') 

def RegistrarMascota(request):
    return render(request, 'core/registrarMascota.html')

def cartilla(request):
    return render(request, 'core/cartilla.html')

def editar(request):
    return render(request, 'core/editar.html')


