# Generated by Django 4.2.1 on 2023-06-02 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0009_remove_productos_stock'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Productos',
            new_name='Producto',
        ),
        migrations.RenameModel(
            old_name='Vendedor',
            new_name='Vendedores',
        ),
    ]