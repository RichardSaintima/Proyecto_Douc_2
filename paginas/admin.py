from django.contrib import admin

# Register your models here.
from .models import  Cliente, Genero, Vendedor

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Genero)
admin.site.register(Vendedor)