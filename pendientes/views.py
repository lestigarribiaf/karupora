from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    saludo = "<h1> Hola, Mundo! </h1> Esta es la raiz / Tuhermanaentanga"
    return HttpResponse(saludo) #retornamos el saludo

def tarea(request):
    return HttpResponse("<h2>Hola soy la vista Tarea</h2> <br> <h6> Y realmente estoy muy al pedo pero... bue <h6>")

def informacion(request):
    return HttpResponse("<h1> Esto es una info </h1> <br> <img src='../django_todo_template/mamadice.jpg' alt 'keonda ndoikoi nio'> <br>  <p> <li> Your work is going to fill to do what you believe is great work. And the only way to do great work is to love what you do. <br> If you havent found it yet, keep looking. Dont settle. As with all matters of the heart, youll know when you find it.</p> ")