from django.contrib import admin
from .models import  Cliente, Genero, Vendedor, Categoria, Productos
# Register your models here.

class clienteAdmin(admin.ModelAdmin) :
    list_display =['nombre', 'apellido_paterno', 'apellido_materno',  'telefono',  'email']
    search_fields = ['email']
    list_per_page = 10

class vendedorAdmin(admin.ModelAdmin) :
    list_display =['rut', 'nombre', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento',
     'id_genero','imagen', 'telefono', 'email', 'direccion', 'activo']
    list_editable =['imagen', 'email', 'direccion', 'activo']
    list_per_page = 2

class productoAdmin(admin.ModelAdmin) :
    list_display =['id_producto', 'titulo', 'precio', 'imagen', 'descripcion',
     'stock','id_categoria']  
    list_filter =['id_categoria', 'precio']
    list_per_page = 2
    list_editable =['imagen']

# Register your models here.
admin.site.register(Cliente, clienteAdmin)
admin.site.register(Genero)
admin.site.register(Vendedor, vendedorAdmin)
admin.site.register(Categoria)
admin.site.register(Productos, productoAdmin)