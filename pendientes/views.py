from django.shortcuts import render
from django.http import HttpResponse
from pendientes.models import Receta

# Create your views here.

def index(request):
    usuario = request.GET.get("user")
    print(request.GET)
    saludo = "<h1> Hola, Mundo! </h1> Esta es la raiz "
    return HttpResponse(usuario) #retornamos el saludo

def recetas(request):
    lista = Receta.objects.all()
    listita = {'name':lista}
    recorrido = 0
    for x in lista:
        recorrido = x
    return render(request, 'index.html', listita)

def registro(request):
        return render(request, 'registro.html')

