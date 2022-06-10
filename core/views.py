from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

# Vistas usuario anonimo
def redirect_to_root (request):
    return HttpResponseRedirect('index')

def index(request):
    return render(request, 'core/index.html')

def login(request):
    return render(request, 'core/cred/login.html')

def signin(request):
    return render(request, 'core/cred/signin.html')

# Vistas usuario normal
def cli_index(request):
    return render(request, 'core/cli/index.html')

def buscar_sucursal(request):
    return render(request, 'core/cli/buscar_sucursal.html')

def registrarMascota(request):
    return render(request, 'core/cli/registrarMascota')

# Vistas usuario veterinario
def vet_index(request):
    return render(request, 'core/vet/index.html')

def registrarCartillaMedica(request):
    return render(request, 'core/vet/registraCartilla.html')

# Vistas usuario secretario
def sec_index(request):
    return render(request, 'core/sec/index.html')

def gestionarAtenciones(request):
    return render(request, 'core/sec/administrar')

def editarAtencion(request):
    return render(request, 'core/sec/editar.html')

# ! No se utiliza por el momento
# Vistas usuario administrativo
def admin_index(request):
    return render(request, 'core/admin/index.html')