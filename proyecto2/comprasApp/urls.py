from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from comprasApp.views import Vista_comprar, Vista_lista_compras


urlpatterns = [
    path('<int:id>', login_required(Vista_comprar.as_view()), name='comprar'),
    path('listaCompras', Vista_lista_compras.as_view(), name= "listaCompras")
]