from django.shortcuts import render, redirect,  reverse
from .custom_auth import custom_authenticate, custom_login, custom_logout
from paginas.models import Categoria, Genero, Producto, Persona
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages



# Create your views here.
def index(request) : 
    productos = Producto.objects.all()
    context ={"productos" : productos}
    return render(request, 'paginas/session/index.html', context)


def nosotros(request) :
    context ={}
    return render(request, 'paginas/session/nosotros.html', context)

def contacto(request) :
    context = {}
    return render(request, 'paginas/contactos/contacto.html', context)


def login_v(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            persona = Persona.objects.get(email=email)

            if persona.password == password:
                custom_login(request, persona)
                if persona.is_vendedor:
                    return redirect('vendedor/')
                else:
                    return redirect('/')
            else:
                messages.error(request, 'Credenciales inválidas')
                context = {}
                return render(request, 'paginas/auth/login.html', context)

        except Persona.DoesNotExist:
            messages.error(request, 'Credenciales inválidas')
            context = {}
            return render(request, 'paginas/auth/login.html', context)

    context = {}
    return render(request, 'paginas/auth/login.html', context)


def logout_v(request):
    custom_logout(request)
    return redirect('/')



def signup(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        genero_id = request.POST['genero']
        telefono = request.POST['telefono']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if Persona.objects.filter(email=email).exists():
            generos = Genero.objects.all()
            mensaje = "Usuario ya existe"
            context = {
                'mensaje': mensaje,
                'generos': generos,
            }
            return render(request, 'paginas/auth/signup.html', context)

        if password != password2:
            generos = Genero.objects.all()
            mensaje = "Las contraseñas no coinciden"
            context = {
                'mensaje': mensaje,
                'generos': generos,
            }
            return render(request, 'paginas/auth/signup.html', context)

        genero = Genero.objects.get(id_genero=genero_id)

        persona = Persona(
            nombre=nombre,
            apellido=apellido,
            id_genero=genero,
            telefono=telefono,
            email=email,
            password=password
        )
        persona.save()

        messages.success(request, 'Registro exitoso. Inicia sesión para continuar.')
        return redirect('/login')
    else:
        generos = Genero.objects.all()
        context = {'generos': generos}
        return render(request, 'paginas/auth/signup.html', context)



def producto(request):
    if 'carrito' in request.session:
        carrito = request.session['carrito'] 
        context = {
                'carrito': carrito,
                }
        return render(request, 'paginas/productos/producto.html', context)
    else:
        carrito = []
        context = {
                'carrito': carrito,
                }
    return render(request, 'paginas/productos/producto.html', context)



def crear(request) :
    if request.method == "GET":
        categorias = Categoria.objects.all()
        context ={'categorias' : categorias}
        return render(request, 'paginas/productos/producto_crear.html', context)
    else:
        print(request.POST)
        titulo=request.POST['titulo']
        precio=request.POST['precio']
        imagen = request.FILES['imagen']
        descripcion=request.POST['descripcion']
        categoria=request.POST['categoria']

        objCategoria=Categoria.objects.get(id_categoria=categoria)
        obj=Producto.objects.create(
            titulo=titulo,
            precio=precio,
            imagen=imagen,
            descripcion=descripcion,
            id_categoria=objCategoria)    
        obj.save()
        messages.success(request, 'Agregado Correctamente.')
        return redirect( '/vendedor/')



def eliminar(request,pk):
    context ={}
    try:
        producto=Producto.objects.get(id_producto=pk)

        producto.delete()
        mensaje= "Eliminado Correctamente"
        productos=Producto.objects.all()
        context ={'productos' : productos, 'mensaje' : mensaje,}
        return render(request, 'paginas/trabajadores/vendedor.html', context)
    except:
        mensaje= "Error, Producto no existe"
        productos=Producto.objects.all()
        context ={'productos' : productos, 'mensaje' : mensaje,}
        return render(request, 'paginas/trabajadores/vendedor.html', context)



def actualizar(request,pk):

    if pk != "":
        producto=Producto.objects.get(id_producto=pk)
        categorias = Categoria.objects.all()

        print(type(producto.id_categoria.categoria))
        context ={'producto' : producto, 'categorias' : categorias}
        if producto:
            return render(request, 'paginas/productos/producto_edit.html', context)

        else:
            context={'mensaje': "Error, Producto no existe"}
            return render(request, 'paginas/trabajadores/vendedor.html', context)



def productoUpdate(request, pk):
    if request.method == "POST":
        titulo = request.POST['titulo']
        precio = request.POST['precio']
        imagen = request.FILES['imagen']
        descripcion = request.POST['descripcion']
        categoria = request.POST['categoria']

        objCategoria = Categoria.objects.get(id_categoria=categoria)

        producto = Producto.objects.get(id_producto=pk)
        producto.titulo = titulo
        producto.precio = precio
        producto.imagen = imagen
        producto.descripcion = descripcion
        producto.id_categoria = objCategoria
        producto.save()

        categorias = Categoria.objects.all()
        messages.success(request,"Producto Actualizado Correctamente")
        return redirect('vendedor')
    else:
        producto = Producto.objects.get(id_producto=pk)
        categorias = Categoria.objects.all()
        context = {
            'producto': producto,
            'categorias': categorias
        }
        return render(request, 'paginas/productos/producto_edit.html', context)



def comprar(request, pk):
    producto = get_object_or_404(Producto, id_producto=pk)
    context = {'producto': producto}
    return render(request, 'paginas/productos/comprar.html', context)

def verificaCompra(request) :
    context ={}
    return render(request, 'paginas/compra/verificar.html', context)


@login_required
def vendedor(request) :
    productos = Producto.objects.all()
    context ={"productos" : productos}
    return render(request, 'paginas/trabajadores/vendedor.html', context)

def sorry(request) :
    context ={}
    return render(request, 'extras/sorry.html', context)
