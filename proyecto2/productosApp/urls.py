from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from productosApp.views import Vista_productos, Vista_crear_producto, Vista_listado_productos, Vista_editar_producto

urlpatterns = [
    path('', Vista_productos.as_view(), name= "listaProductos"),
    path('listadoProductos', login_required(Vista_listado_productos.as_view()), name= "listadoProductos"),
    path('crearProducto', login_required(Vista_crear_producto.as_view()), name= "crearProducto"),
    path('editarProducto/<int:id>', login_required(Vista_editar_producto.as_view()), name= "editarProducto"),
    
    
]