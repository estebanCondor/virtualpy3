from django.http import HttpResponse
from django.template import Template, Context

def saludo(request): # Primera vista
    return HttpResponse("Hola, primera pagina con Django")

def plantilla(request):
    return HttpResponse("Hola, segunda pagina con Django")
    plantilla_externa= loader.get_template('principal.html')
    contexto = Context
    # Renderizar el documento
    documento = plantilla_externa.render(contexto)
    return HttpResponse(documento)