# KARU PORÃ

### Sitio de Consultas de Recetas y Planeamiento Semanal > addons:

* Listado de Recetas. LISTO
* Vista de Recetas individual > Lista + preparacion + ingredientes LISTO
* Planeamiento semanal. EN PROCESO
* Calculo de precios aproximados. SI SOBRA TIEMPO

### Objetivos de disenho: 

* Cargar todas las skins. (Editar Textos, Subir imagenes) LISTO
* Subida completa en facebook, instagram, y listado recetas LISTO 
* Arreglar la web principal con los espaciados, verificar codigo section or div


### Objetivos de funcionalidad: 

* Subir imagenes de la lista dentro del /admin LISTO
* Trazar nueva template para Vista Receta Individual LISTO
* Hacer que estire en el menu planificacion los valores de comidas + buscador TODAVIA 
* Hacer que estire desde /semanal se pueda estirar los valores en un combo-box (for dentro del select-option-value)

### Objetivos de Marketing: 

* Portada / Subida de imagenes en el sitio LISTO
* Invitar a tus amigos TODAVIA
* Subir todas las fotex con nuestros rostros umia. EN PROCESO

### Pasos para poder montar el mismo servicio en tu compu:

* En la terminal:
```bash
pip3 install django==2.2 #instalamos django con pip(manejador de paquetes de python)
django-admin startproject todolist #creamos el proyecto todolist
cd todolist #entramos al directorio
python3 manage.py startapp pendientes #se crea la app pendientes(un proyecto puede tener muchas apps)
#todolist/settings.py -> agregar 'pendientes' a installed apps
#pendientes/models.py -> Crear modelo/tabla Tarea
#pendientes/models.py -> Registar modelo Tarea en la interfaz de Administracion
python3 manage.py makemigrations #se crea el archivo de migracion de base de datos
python3 manage.py migrate #guardamos los cambios en la base de datos(archivo db.sqlite3)
python3 manage.py createsuperuser #se crea un usuario administrador, en este caso admin:admin

python3 manage.py runserver #corremos el servidor de desarrollo
# Abrir el navegador en http:localhost:8000
# http:localhost:8000/admin para la interfaz de administracion
```

* en `todolist/settings.py`:
  * se agrega `'pendientes'` a `INSTALLED_APPS`
  * se cambia el idioma a español

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pendientes' #esta linea es la que agregamos
]
```
```python
LANGUAGE_CODE = 'es'
``` 

* en `pendientes/models.py` creamos el modelo Recetas (modelo ~= tabla de la base de datos)

* O si no, podes directamente clonar este repositorio. Navega hasta la carpeta donde vas a copiar y:


```python
git clone https://github.com/lestigarribiaf/karupora.git
```