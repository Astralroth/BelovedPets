from django.urls import path

from core.views import admin_index, cli_index, crearAtencion, editarAtencion, gestionarAtenciones, index, login, redirect_to_root, registrarCartillaMedica, sec_index, signin, solicitarAtencion, vet_index, registrarMascota

#Urls usuario anonimo
urlpatterns = [
    path('', redirect_to_root, name='redirect_to_root'),
    path("index/", index, name="index"),
    path('login/', login, name='login'),
    path('signin/', signin, name='signin'),
]

# Urls usuario normal
urlpatterns+=[
    path("cli/index/", cli_index, name="cli_index"),
    path('cli/sol/att', solicitarAtencion, name='solicitar_atencion'),
    path('cli/add/pet/', registrarMascota, name="registrar_mascota"),
]

#Urls usuario veterinario
urlpatterns+=[
    path('vet/index/', vet_index, name="vet_index"),
    path('vet/add/cart', registrarCartillaMedica, name='registrar_cartilla')
]

#Urls usuario secretario
urlpatterns+=[
    path('sec/index/', sec_index, name="sec_index"),
    path('sec/list/att', gestionarAtenciones, name="gestionar_atenciones"),
    path('sec/edit/att', editarAtencion, name="editar_atencion"),
    path('sec/add/att', crearAtencion, name="crear_atencion"),
]

# ! No se usa por el momento
#Urls usuario administrativo
urlpatterns+=[
    path('admin/index/', admin_index, name="admin_index")
]