
from django.contrib import admin
from paginas.models import Categoria, Genero, Producto, Persona, Carrito
# Register your models here.

class personaAdmin(admin.ModelAdmin) :
    list_display =['id_persona', 'nombre', 'apellido', 
     'id_genero', 'telefono', 'email','password','is_vendedor']
#     # list_per_page = 2
    list_editable =['is_vendedor']

class productoAdmin(admin.ModelAdmin) :
    list_display =['id_producto', 'titulo', 'precio', 'imagen', 'descripcion',
    'id_categoria']  
#     # list_filter =['id_categoria', 'precio']
class carritoAdmin(admin.ModelAdmin) :
    list_display =['id_carrito','id_producto', 'precio', 'descripcion_producto',]  
#     # list_filter =['id_categoria', 'precio']
#     list_per_page = 10
#     
    

# Register your models here.

admin.site.register(Genero)
admin.site.register(Persona , personaAdmin)
admin.site.register(Categoria)
admin.site.register(Producto, productoAdmin)
admin.site.register(Carrito, carritoAdmin)
