from django.urls import path

from core.views import index, login, redirect_to_root


urlpatterns = [
    path('', redirect_to_root, name='redirect_to_root'),
    path('index/', index, name='index'),
    path('login/', login, name='login'),
]
