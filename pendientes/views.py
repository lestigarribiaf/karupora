from django.shortcuts import render
from django.http import HttpResponse
from pendientes.models import Receta

# Create your views here.

def index(request):
    saludo = "<h1> Hola, Mundo! </h1> Esta es la raiz / Tuhermanaentanga"
    return HttpResponse(saludo) #retornamos el saludo

def recetas(request):
    lista = Receta.objects.all()

    listita = {'name':lista}
    return render(request, 'index.html', listita)
