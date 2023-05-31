from django.shortcuts import render

# Create your views here.
def index(request) :
    # alumnos = Alumno.objects.all()
    context ={}
    return render(request, 'paginas/session/index.html', context)
def nosotros(request) :
    # alumnos = Alumno.objects.all()
    context ={}
    return render(request, 'paginas/session/nosotros.html', context)

def contacto(request) :
    context = {}
    return render(request, 'paginas/contactos/contacto.html', context)

def login(request) :
    # alumnos = Alumno.objects.all()
    context ={}
    return render(request, 'paginas/auth/login.html', context)
def signup(request) :
    # alumnos = Alumno.objects.all()
    context ={}
    return render(request, 'paginas/auth/signup.html', context)
def producto(request) :
    # alumnos = Alumno.objects.all()
    context ={}
    return render(request, 'paginas/productos/producto.html', context)
def vendedor(request) :
    # alumnos = Alumno.objects.all()
    context ={}
    return render(request, 'paginas/vendedores/vendedor.html', context)
def sorry(request) :
    # alumnos = Alumno.objects.all()
    context ={}
    return render(request, 'extras/sorry.html', context)

