from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import FormView
from django.urls import reverse_lazy
from . import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from productosApp.models import Producto
from comprasApp.models import Compra

# Create your views here.
class Vista_comprar(PermissionRequiredMixin, FormView):
    permission_required = 'productosApp.comprar_productos'
    
    def handle_no_permission(self):
        return redirect('listaProductos')
    
    template_name = "registrarCompra.html"
 
    form_class = forms.Form_registrar_compra
    success_url = reverse_lazy('listaCompras')
        

    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        id = self.kwargs.get('id')
        producto = get_object_or_404(Producto, id = id)
        kwargs['instance'] = producto
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get('id')
        producto = get_object_or_404(Producto, id=id)
        context['producto'] = producto
        return context
    

    def form_valid(self, form):
        form.save(self.kwargs.get('id'), user = self.request.user)
        return super().form_valid(form)
    
class Vista_lista_compras(TemplateView):
    template_name = 'listaCompras.html'
    def get_context_data(self):
        compras = Compra.objects.filter(cliente = self.request.user.id)

        return {
            'compras': compras
        }
        