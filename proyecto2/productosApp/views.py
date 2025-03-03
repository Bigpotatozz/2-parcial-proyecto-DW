from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from productosApp.models import Producto
from . import forms

# Create your views here.

class Vista_productos(TemplateView):
    template_name = "vistaProductos.html"
    def get_context_data(self):
        productos = Producto.objects.all()
        
        return {
            "productos": productos
        }
        
class Vista_listado_productos(PermissionRequiredMixin,TemplateView):
    permission_required = "productosApp.administrador"
    
    template_name = "listadoProductos.html"
    def handle_no_permission(self):
        return redirect('listaProducto')
    
    def get_context_data(self):
        productos = Producto.objects.all()
        
        return {
            "productos": productos
        }
    
        
class Vista_crear_producto(PermissionRequiredMixin, FormView):
    
    permission_required = "productosApp.administrador"
    
    def handle_no_permission(self):
        return redirect('listaProducto')
    
    template_name = "crearProducto.html"
    form_class = forms.Form_registrar_producto
    success_url = reverse_lazy('listaProductos')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class Vista_editar_producto(PermissionRequiredMixin, FormView):
    permission_required = "productosApp.administrador"
    def handle_no_permission(self):
        return redirect('listaProducto')
    
    template_name = "editarProducto.html"
    form_class = forms.Form_editar_producto
    success_url = reverse_lazy('listadoProductos')
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        id = self.kwargs.get('id')
        producto = get_object_or_404(Producto, id = id)
        kwargs['instance'] = producto
        return kwargs
    
    def form_valid(self, form):
        form.save(self.kwargs.get('id'))
        return super().form_valid(form)