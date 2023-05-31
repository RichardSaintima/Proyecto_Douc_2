from django.shortcuts import render
from .models import Categoria, Cliente, Genero, Productos, Vendedor

# Create your views here.
def index(request) :
    productos = Productos.objects.all()
    context ={"productos" : productos}
    return render(request, 'paginas/session/index.html', context)

def nosotros(request) :
    context ={}
    return render(request, 'paginas/session/nosotros.html', context)

def contacto(request) :
    context = {}
    return render(request, 'paginas/contactos/contacto.html', context)

def login(request) :
    context ={}
    return render(request, 'paginas/auth/login.html', context)

def signup(request) :
    context ={}
    return render(request, 'paginas/auth/signup.html', context)

def producto(request) :
    context ={}
    return render(request, 'paginas/productos/producto.html', context)

def vendedor(request) :
    context ={}
    return render(request, 'paginas/trabajadores/vendedor.html', context)

def sorry(request) :
    context ={}
    return render(request, 'extras/sorry.html', context)

