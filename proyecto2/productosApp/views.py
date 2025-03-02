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
        
class Vista_crear_producto(FormView):
    template_name = "crearProducto.html"
    form_class = forms.Form_registrar_producto
    success_url = reverse_lazy('listaProductos')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)