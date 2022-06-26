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

def registrarMascota(request):
    return render(request, 'core/cli/registrarMascota.html')

def solicitarAtencion(request):
    return render(request, 'core/cli/solicitarAtencion.html')

def solicitarAtencionRapida(request):
    return render(request, 'core/cli/solicitarAtencionRapida.html')

def mascotaExtraviadaCli(request):
    return render(request, 'core/cli/masExtraviada.html')

def publicarRuta(request):
    return render(request, 'core/admin/publicarRuta.html')

def publicarPaseo(request):
    return render(request, 'core/admin/publicarPaseo.html')

def listarPaseos(request):
    return render(request, 'core/admin/listarPaseos.html')


# Vistas usuario veterinario
def vet_index(request):
    return render(request, 'core/vet/index.html')

def registrarCartillaMedica(request):
    return render(request, 'core/vet/registrarCartilla.html')

def listarAtenciones(request):
    return render(request, 'core/vet/listarAtenciones.html')

def atencion(request):
    return render(request, 'core/vet/atencion.html')

def atencionRapida(request):
    return render(request, 'core/vet/atencionRapida.html')

def mascotaExtraviadaVet(request):
    return render(request, 'core/vet/masExtraviada.html')


# Vistas usuario secretario
def sec_index(request):
    return render(request, 'core/sec/index.html')

def gestionarAtenciones(request):
    return render(request, 'core/sec/administrar.html')

def editarAtencion(request):
    return render(request, 'core/sec/editar.html')

def crearAtencion(request):
    return render(request, 'core/sec/crearAtencion.html')


# ! No se utiliza por el momento
# Vistas usuario administrativo
def admin_index(request):
    return render(request, 'core/admin/index.html')