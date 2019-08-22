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

def lista_recetas(request):
        queryset = Receta.objects.all() #lista de los objetos
        context = {
                "lista_objetos" : queryset
        }
        print(queryset)
        return render(request, 'lista_recetas.html', context)


def semanal(request):
        queryset = Receta.objects.all() #lista de los objetos
        context = {
                "lista_objetos" : queryset
        }
        return render(request, 'semanal.html',context)

def resumen(request):
        return render(request, 'resumen.html')


def receta_detalles(request, num):
        receta = Receta.objects.get(id=num)

        return render(request, 'vista_receta.html', {"receta":receta})

def busqueda(request, buscar):
        buscarte = Receta.objects.filter(nombre_receta__icontains=buscar)
        print (buscarte)        

        return render(request, 'semanal.html' , {"busquedaes":buscarte})


def impresion(request):
        datos=request.POST 
        cena_lunes = datos.get("cenaLunes")
        almuerzo_lunes = datos.get("almuerzoLunes")
        cena_martes = datos.get("cenaMartes")
        print(cena_lunes)
        context = {
                "cena_lunes" : cena_lunes , 
                "almuerzo_lunes": almuerzo_lunes,
                "cena_martes" : cena_martes
                }
        
        return render(request, 'impresion.html', context)