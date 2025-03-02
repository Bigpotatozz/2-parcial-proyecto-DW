from django import forms
from comprasApp.models import Compra
from productosApp.models import Producto

class Form_registrar_compra(forms.ModelForm):

    cantidad = forms.IntegerField()
    
    class Meta:
        model = Compra
        fields =  ['cantidad']
        
    def save(self, id, user):
        producto = Producto.objects.filter(id = id).get()
        cantidad = self.cleaned_data['cantidad']
        
        
        new_compra = Compra(cantidad = cantidad, 
                            precio = cantidad * producto.precio,
                            cliente = user,
                            producto = producto)
        
        new_compra.save()
        
        
        
        
        
        