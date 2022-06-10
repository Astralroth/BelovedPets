from django.urls import path

from core.views import  editar, cartilla, RegistrarMascota,Administrar, index, login, redirect_to_root


urlpatterns = [
    path('', redirect_to_root, name='redirect_to_root'),
    path('index/', index, name='index'),
    path('login/', login, name='login'),
    path('administrar/', Administrar, name='administrar'),
    path('registrarMascota/', RegistrarMascota, name='registrarMascota'),
    path('cartilla/', cartilla, name='cartilla'),
    path('editar/', editar, name='editar'),
]
