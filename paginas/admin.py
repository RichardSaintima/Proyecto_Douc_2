from django.contrib import admin
from paginas.models import Categoria, Genero, Producto, Persona
# Register your models here.

# class personaAdmin(admin.ModelAdmin) :
#     list_display =['id_persona', 'nombre', 'apellido', 
#      'id_genero', 'telefono', 'email','password','is_vendedor']
#     # list_per_page = 2

# class productoAdmin(admin.ModelAdmin) :
#     list_display =['id_producto', 'titulo', 'precio', 'imagen', 'descripcion',
#     'id_categoria']  
#     # list_filter =['id_categoria', 'precio']
#     list_per_page = 10
#     # list_editable =['imagen']
    

# Register your models here.

admin.site.register(Genero)
admin.site.register(Persona)
admin.site.register(Categoria)
admin.site.register(Producto)
