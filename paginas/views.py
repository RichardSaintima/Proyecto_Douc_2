from django.shortcuts import render, redirect,  reverse
from paginas.custom_auth import custom_authenticate, custom_login, custom_logout, login_required
from paginas.models import Categoria, Genero, Producto, Persona, Carrito
from django.shortcuts import render, get_object_or_404
from django.contrib import messages



# Create your views here.
def index(request) :
    if 'id_persona' in request.session:
        persona = Persona.objects.get(id_persona=request.session['id_persona']) 
        productos = Producto.objects.all()
        context ={"productos" : productos,
                  "persona": persona}
        return render(request, 'paginas/session/index.html', context)
    productos = Producto.objects.all()
    context ={"productos" : productos,}
    return render(request, 'paginas/session/index.html',context)


def nosotros(request):
    if 'id_persona' in request.session:
        persona = Persona.objects.get(id_persona=request.session['id_persona'])
        if not persona.is_vendedor:
            context = {"persona": persona}
            return render(request, 'paginas/session/nosotros.html', context)
    return render(request, 'paginas/session/nosotros.html')


def contacto(request) :
    if 'id_persona' in request.session:
        persona = Persona.objects.get(id_persona=request.session['id_persona'])
        if not persona.is_vendedor:
            context = {"persona": persona}
            return render(request, 'paginas/contactos/contacto.html', context)
    return render(request, 'paginas/contactos/contacto.html')


def login_v(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            persona = custom_authenticate(email, password)

            if persona is not None:
                custom_login(request, persona)
                if persona.is_vendedor:
                    return redirect('/vendedor/')
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
    if 'id_persona' in request.session:
        persona = Persona.objects.get(id_persona=request.session['id_persona'])
        if not persona.is_vendedor:
            productos = Carrito.objects.all()
            context = { 'persona': persona,
               'productos': productos}
            return render(request, 'paginas/productos/producto.html', context)
    productos = Carrito.objects.all()
    context = { 'productos': productos}
    return render(request, 'paginas/productos/producto.html', context)



def crear(request):
    if request.method == "GET":
        categorias = Categoria.objects.all()
        context = {'categorias': categorias}
        return render(request, 'paginas/productos/producto_crear.html', context)
    else:
        titulo = request.POST.get('titulo')
        precio = request.POST.get('precio')
        imagen = request.FILES.get('imagen')
        descripcion = request.POST.get('descripcion')
        categoria = request.POST.get('categoria')

        if not titulo:
            messages.error(request, 'El campo de título es obligatorio.')
            categorias = Categoria.objects.all()
            context = {'categorias': categorias}
            return render(request, 'paginas/productos/producto_crear.html', context)
        if not precio:
            messages.error(request, 'El campo de precio es obligatorio.')
            messages.error(request, 'El campo de título es obligatorio.')
            categorias = Categoria.objects.all()
            context = {'categorias': categorias}
            return render(request, 'paginas/productos/producto_crear.html', context)
        if not imagen:
            messages.error(request, 'Debe seleccionar una imagen.')
            messages.error(request, 'El campo de título es obligatorio.')
            categorias = Categoria.objects.all()
            context = {'categorias': categorias}
            return render(request, 'paginas/productos/producto_crear.html', context)
        if not descripcion:
            messages.error(request, 'El campo de descripción es obligatorio.')
            return redirect('crear')
        if not categoria:
            messages.error(request, 'Debe seleccionar una categoría.')
            messages.error(request, 'El campo de título es obligatorio.')
            categorias = Categoria.objects.all()
            context = {'categorias': categorias}
            return render(request, 'paginas/productos/producto_crear.html', context)

        objCategoria = Categoria.objects.get(id_categoria=categoria)

        obj = Producto.objects.create(
            titulo=titulo,
            precio=precio,
            imagen=imagen,
            descripcion=descripcion,
            id_categoria=objCategoria
        )
        obj.save()

        messages.success(request, 'Producto agregado correctamente.')
        return redirect('/vendedor/')



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
    
def eliminarCarrito(request, carrito_pk):
    carrito = get_object_or_404(Carrito, id_carrito=carrito_pk)
    carrito.delete()
    return redirect('producto') 



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
        titulo = request.POST.get('titulo')
        precio = request.POST.get('precio')
        imagen = request.FILES.get('imagen')
        descripcion = request.POST.get('descripcion')
        categoria = request.POST.get('categoria')

        # Validación de campos
        if not titulo:
            messages.error(request, 'El campo de título es obligatorio.')
            producto = Producto.objects.get(id_producto=pk)
            categorias = Categoria.objects.all()
            context = {
                'producto': producto,
                'categorias': categorias
            }
            return render(request, 'paginas/productos/producto_edit.html', context)
        if not precio:
            messages.error(request, 'El campo de precio es obligatorio.')
            producto = Producto.objects.get(id_producto=pk)
            categorias = Categoria.objects.all()
            context = {
                'producto': producto,
                'categorias': categorias
            }
            return render(request, 'paginas/productos/producto_edit.html', context)
        if not imagen:
            messages.error(request, 'Debe seleccionar una imagen.')
            producto = Producto.objects.get(id_producto=pk)
            categorias = Categoria.objects.all()
            context = {
                'producto': producto,
                'categorias': categorias
            }
            return render(request, 'paginas/productos/producto_edit.html', context)
        if not descripcion:
            messages.error(request, 'El campo de descripción es obligatorio.')
            producto = Producto.objects.get(id_producto=pk)
            categorias = Categoria.objects.all()
            context = {
                'producto': producto,
                'categorias': categorias
            }
            return render(request, 'paginas/productos/producto_edit.html', context)
        if not categoria:
            messages.error(request, 'Debe seleccionar una categoría.')
            producto = Producto.objects.get(id_producto=pk)
            categorias = Categoria.objects.all()
            context = {
                'producto': producto,
                'categorias': categorias
            }
            return render(request, 'paginas/productos/producto_edit.html', context)

        objCategoria = Categoria.objects.get(id_categoria=categoria)

        producto = Producto.objects.get(id_producto=pk)
        producto.titulo = titulo
        producto.precio = precio
        if imagen:
            producto.imagen = imagen
        producto.descripcion = descripcion
        producto.id_categoria = objCategoria
        producto.save()

        messages.success(request, 'Producto actualizado correctamente.')
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
    if 'id_persona' in request.session:
        persona = Persona.objects.get(id_persona=request.session['id_persona'])
        if not persona.is_vendedor:
            producto = get_object_or_404(Producto, id_producto=pk)
            context = { 'persona': persona,
                'producto': producto}
            return render(request, 'paginas/productos/comprar.html', context)
    producto = get_object_or_404(Producto, id_producto=pk)
    context = {'producto': producto}
    return render(request, 'paginas/productos/comprar.html', context)

def carrito(request, producto_pk):
    producto = Producto.objects.get(id_producto=producto_pk)
    carrito = Carrito(
        id_producto=producto,
        precio=producto.precio,
        nombre_producto=producto.titulo,
        descripcion_producto=producto.descripcion
    )
    carrito.save()
    productos = Carrito.objects.all()
    context = {"productos": productos}
    return redirect( 'producto')




@login_required
def verificaCompra(request) :
    context ={}
    return render(request, 'paginas/compra/verificar.html', context)


@login_required
def vendedor(request):
    persona = Persona.objects.get(id_persona=request.session['id_persona'])
    if persona.is_vendedor:
        productos = Producto.objects.all()
        context = {"productos": productos, "persona": persona}
        return render(request, 'paginas/trabajadores/vendedor.html', context)
    else:
        return redirect('/')

    
@login_required
def vendedorIndex(request):
    persona = Persona.objects.get(id_persona=request.session['id_persona'])
    if persona.is_vendedor:
        productos = Producto.objects.all()
        context = {"productos": productos, "persona": persona}
        return render(request, 'paginas/trabajadores/index.html', context)
    return render(request, 'paginas/trabajadores/index.html')

def sorry(request) :
    if 'id_persona' in request.session:
        persona = Persona.objects.get(id_persona=request.session['id_persona'])
        if not persona.is_vendedor:
            context = {"persona": persona}
            return render(request, 'extras/sorry.html', context)
    return render(request, 'extras/sorry.html')
