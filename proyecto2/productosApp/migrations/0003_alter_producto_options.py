# Generated by Django 5.1.5 on 2025-03-02 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productosApp', '0002_alter_producto_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producto',
            options={'permissions': [('comprar_productos', 'puede comprar productos'), ('administrador', 'puede editar y agregar productos')]},
        ),
    ]
