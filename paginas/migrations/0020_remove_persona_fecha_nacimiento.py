# Generated by Django 4.2.1 on 2023-06-03 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0019_persona_delete_cliente_alter_producto_imagen_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='fecha_nacimiento',
        ),
    ]