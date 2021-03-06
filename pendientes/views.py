from django.shortcuts import render
from django.http import HttpResponse
from pendientes.models import Receta
# Create your views here.

def index(request):
    usuario = request.GET.get("user")
    print(request.GET)
    saludo = "<h1> Hola, Mundo! </h1> Esta es la raiz "
    return HttpResponse(saludo) #retornamos el saludo

def recetas(request):
    lista = Receta.objects.all()
    listita = {'name':lista}
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

def main_Template(request): #Pagina que va a mostar algunos elementos cargados en el index
        queryset = Receta.objects.all() #lista de los objetos
        context = {
                "lista_objetos" : queryset
        }
        print(queryset)
        return render(request, 'maintemplate.html', context)

def semanal(request):
        queryset = Receta.objects.all() #lista de los objetos
        context = {
                "lista_objetos" : queryset
        }
        return render(request, 'semanal.html',context)

def receta_detalles(request, num):
        receta = Receta.objects.get(id=num)
        cantidad_total = []
        for ingrediente in receta.insumos.all():
                #Descubri ACA COMO SE CONECTA CON EL VISTARECETA.HTML Y SU MODELS ES INSUMO.
                cantidad_total.append(ingrediente.cantidad_insumo)
                print(cantidad_total) #Veo que existe la lista 
        mult2= 0
        for x in cantidad_total: #Recorro uno por uno
                mult2 = x * 2 
                
        mult10=0
        for x in cantidad_total: #DESCUBRI QUE SOLO ME MUESTRA EL ULTIMO DATO DEL FOR. WHY? NPI
                #AVERIGUARCOMO ARREGLAR MAÑANA
                mult10 = x * 10
                        
        return render(request, 'vista_receta.html', {'receta':receta, 'dictionario':{'totalx2':mult2, 'totalx10': mult10} })

def busqueda(request, buscar):
        buscarte = Receta.objects.filter(nombre_receta__icontains=buscar)
        print (buscarte)        

        return render(request, 'semanal.html' , {"busquedaes":buscarte})


def impresion(request):
        datos=request.POST 
        print(datos)
        cena_lunes = datos.get("cenaLunes")
        almuerzo_lunes = datos.get("almuerzoLunes")
        cena_martes = datos.get("cenaMartes")
        almuerzo_martes = datos.get("almuerzoMartes")
        almuerzo_miercoles = datos.get("almuerzoMiercoles")
        cena_miercoles = datos.get("cenaMiercoles")
        almuerzo_jueves = datos.get("almuerzoJueves")
        cena_jueves = datos.get("cenaJueves")
        almuerzo_viernes = datos.get("almuerzoViernes")
        cena_viernes = datos.get("cenaViernes")
        almuerzo_sabado = datos.get("almuerzoSabado")
        cena_sabado = datos.get("cenaSabado")
        almuerzo_domingo = datos.get("almuerzoDomingo")
        cena_domingo = datos.get("cenaDomingo")
        context = {
                "almuerzo_lunes" : almuerzo_lunes , 
                "cena_lunes": cena_lunes,
                "almuerzo_martes" : almuerzo_martes,
                "cena_martes" : cena_martes,
                "almuerzo_miercoles" : almuerzo_miercoles,
                "cena_miercoles" : cena_miercoles,
                "almuerzo_jueves" : almuerzo_jueves,
                "cena_jueves" : cena_jueves,
                "almuerzo_viernes" : almuerzo_viernes,
                "cena_viernes" : cena_viernes,
                "almuerzo_sabado" : almuerzo_sabado,
                "cena_sabado" : cena_sabado,
                "almuerzo_domingo" : almuerzo_domingo,
                "cena_domingo" : cena_domingo,
                }
        
        return render(request, 'impresion.html', context)