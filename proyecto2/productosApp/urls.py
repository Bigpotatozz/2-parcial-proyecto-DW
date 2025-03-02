from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from productosApp.views import Vista_productos, Vista_crear_producto

urlpatterns = [
    path('', Vista_productos.as_view(), name= "listaProductos"),
    path('crearProducto', Vista_crear_producto.as_view(), name= "crearProducto")
    
]