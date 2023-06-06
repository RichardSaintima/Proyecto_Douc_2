from paginas.models import Persona
from django.shortcuts import render, redirect,  reverse
from django.contrib import messages

def custom_authenticate(email, password):
    try:
        persona = Persona.objects.get(email=email)
        if persona.password == password:
            return persona
    except Persona.DoesNotExist:
        pass
    return None


def custom_login(request, persona):
    if persona is not None:
        request.session['id_persona'] = persona.id_persona
    else:
        messages.error(request, 'Verifica tu contraseña o aún no tienes una cuenta.')
        return redirect('login/')

def custom_logout(request):
    request.session.flush()
    request.session.clear()
    request.session.modified = True
    return redirect('/')


def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if 'id_persona' not in request.session:
            messages.error(request, 'Debes iniciar sesión para continuar.')
            return redirect('/login/')
            # return render(request, 'paginas/auth/login.html')
        
        return view_func(request, *args, **kwargs)

    return wrapper