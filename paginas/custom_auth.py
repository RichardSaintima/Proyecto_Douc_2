from paginas.models import Persona

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
        pass

def custom_logout(request):
    request.session.flush()
    request.session.clear()
    request.session.modified = True
