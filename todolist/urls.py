"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pendientes import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'), #Creamos la ruta raiz '' gy la enlazamos con nuestra vista index del archivo views.py
    path('recetas/', views.recetas, name='recetas'),
    path('registro/', views.registro, name='registro'),
    path('lista_recetas/', views.lista_recetas, name='lista_recetas'),
    path('recetas/<int:num>', views.receta_detalles, name="vista_recetas")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
