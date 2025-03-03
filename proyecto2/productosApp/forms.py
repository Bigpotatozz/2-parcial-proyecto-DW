from django import forms
from productosApp.models import Producto

class Form_registrar_producto(forms.ModelForm):

    nombre = forms.CharField(max_length=100)
    precio = forms.FloatField()
    imagen = forms.ImageField()

    
    class Meta: 
        model = Producto
        fields = ['nombre', 'precio', 'imagen']
    def save(self):
        new_producto = Producto(nombre = self.cleaned_data['nombre'], 
                                precio = self.cleaned_data['precio'],
                                imagen = self.cleaned_data['imagen'])
        
        new_producto.save()
        
class Form_editar_producto(forms.ModelForm):
    
    nombre = forms.CharField(max_length=100)
    imagen = forms.ImageField()
    precio = forms.FloatField()
    
    class Meta: 
        model = Producto
        fields = ['nombre', 'imagen', 'precio']
        
    def save(self, id):
        producto = Producto.objects.filter(id = id).get()
        producto.nombre = self.cleaned_data['nombre']        
        producto.imagen = self.cleaned_data['imagen']
        producto.precio = self.cleaned_data['precio']
        
        producto.save()