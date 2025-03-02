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