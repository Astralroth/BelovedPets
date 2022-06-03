from django.urls import path

from core.views import buscar_sucursal, index, login, redirect_to_root, signin


urlpatterns = [
    path('', redirect_to_root, name='redirect_to_root'),
    path('index/', index, name='index'),
    path('login/', login, name='login'),
    path('signin/', signin, name='signin'),
    path('buscar_sucursal/', buscar_sucursal, name='buscar_sucursal'),
]
