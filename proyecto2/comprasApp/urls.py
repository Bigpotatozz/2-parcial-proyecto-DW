from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from comprasApp.views import Vista_comprar, Vista_lista_compras, Vista_lista_ventas


urlpatterns = [
    path('<int:id>', login_required(Vista_comprar.as_view()), name='comprar'),
    path('listaCompras', login_required(Vista_lista_compras.as_view()), name= "listaCompras"),
    path('listaVentas', login_required(Vista_lista_ventas.as_view()), name= "listaVentas"),
    
]