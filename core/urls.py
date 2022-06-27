from django.urls import path

from core.views import admin_index, atencion, atencionRapida, buscarSucursal, cli_index, crearAtencion, editarAtencion, gestionarAtenciones, index, listarAtenciones, listarPaseos, login, mascotaExtraviadaCli, mascotaExtraviadaVet, perfil_cli, publicarPaseo, publicarRuta, redirect_to_root, registrarCartillaMedica, sec_index, signin, solicitarAtencion, solicitarAtencionRapida, vet_index, registrarMascota

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
    path('cli/sol/attr', solicitarAtencionRapida, name='solicitar_atencion_rapida'),
    path('cli/add/pet', registrarMascota, name="registrar_mascota"),
    path('cli/ext/pet', mascotaExtraviadaCli, name="mascota_extraviada_cli"),
    path('cli/add/rute', publicarRuta, name="publicar_ruta"),
    path('cli/add/walk', publicarPaseo, name="publicar_paseo"),
    path('cli/list/walk', listarPaseos, name="listar_paseos"),
    path('cli/profile', perfil_cli, name="perfil_cli"),
    path('cli/seach/suc', buscarSucursal, name="buscar_sucursal"),
]

#Urls usuario veterinario
urlpatterns+=[
    path('vet/index/', vet_index, name="vet_index"),
    path('vet/add/cart', registrarCartillaMedica, name='registrar_cartilla'),
    path('vet/list/att', listarAtenciones, name="listar_atenciones"),
    path('vet/det/att', atencion, name="atencion"),
    path('vet/det/attr', atencionRapida, name="atencion_rapida"),
    path('vet/ext/pet', mascotaExtraviadaVet, name="mascota_extraviada_vet" ),
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