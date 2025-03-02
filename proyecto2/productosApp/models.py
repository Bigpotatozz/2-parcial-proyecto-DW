from django.db import models
from django.utils.timezone import now

# Create your models here.

class Producto(models.Model):
    nombre = models.TextField(max_length=50)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='imagenes/', null= True, blank= True)
    
    
    class Meta:
        permissions = [("comprar_productos", "puede comprar productos")]
    
    def __str__(self):
        return f"{self.id}--{self.nombre}--{self.precio}--{self.imagen}"