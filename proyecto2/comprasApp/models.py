from django.db import models
from productosApp.models import Producto
from django.contrib.auth.forms import User

# Create your models here.

class Compra(models.Model):
    cantidad = models.IntegerField()
    precio = models.FloatField()
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null = False, related_name = "compras_producto")
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, null= False, related_name= "compras_cliente")
    
    def __str__(self):
        return f"{self.id}--{self.cantidad}--{self.precio}--{self.producto}--{self.cliente}"