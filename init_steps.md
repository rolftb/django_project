[Django, Curso de Django para Principiantes](https://youtu.be/T1intZyhXDU?si=7CSKC-P6NlzA1foN)
# Iniciar el ambiente
Extensiones a instalar:

- python
- Material Icon Theme, este sirve para identificar los archivos del proyecto y diferenciarlos
- After Dark, es uitilizado para cambiar el color de visualizador de código

## Create a env**
para installar `virtualenv` que es usado para crear ambientes virtuales
`pip install virtualenv`

con esto se crea el ambiente
`virtualenv venv `

ahora se debe acceder al ambiente con 
windows: `./venv/Scrips/activate.bat`
MAC: `source venv/bin/activate`

luego para alinear el interprete (VScode) se pone en el buscador `>select interprete` y se selecciona el ambiente creado (recomendado por VScode)

Luego se realiza el `pip install django`

se puede revisar la version utilizando `python -m django-admin -version` o iniciando python y utilizando `django.get_version()`, luego de `python import django`

`django-admin startproject <nombre-del-proyecto>`
esto crea el sitio de django, con todos los archivos. Acá se créa el poryecto nuevo, el adminisatrador de proeycto.

En este caso, como ya tenemos una carpeta ya creada, entonces se creará el pryecto, en la carpeta actual sin crear una nueva carpeta dentro de la actual. para ello se utiliza el comando 
`django-admin startproject <nombre-del-proyecto> .` el punto luego del nombre del proyecto indica que creará todo desde el directorio actual.
`django-admin startproject first_web .`


## Ejecución

al realizar el comando `django-admin startproject first_web .`
se crean varios archivos, el archivo inicial `manage.py` es utilizado para lanzar el webapp, para ello se puede lanzar con el siguiente comando: `python manage.py runserver`

al ejecutar el servidor se crea el archivo `db.sqite3` que es donde se aloja la base de datos

ahora pude que tengamos corriendo más de una web app, por ello se puede definir el puerto asi `python manage.py runserver 3000` se definión el purto `3000`

## Estructura del proyecto

`manage.py` es utilizada para ejecutar programas administratuivos, como anteriormente se mostró que sirvió para montar un servidor `python manage.py runserver 3000`

al ejecutar el comando `python manage.py --help` muestra todo los comandos que este archivo posee, para lanzar nuevas cosas, como montar un servidor, crear nuevos usuarios administrativos (`createsuperuser`)etc.


 `db.sqlite3` es la base de datos utilizada en desarrollo, para el paso a prod, se debe realizar un cambio y definir algo más formal. pero django se hace cargo de ese cambio.

### mysite (`./mysite`)
 
`__init__.py `, indica que la carpeta es un modulo de python, este archivo viene vacio

`first_web/settings.py ` esta asociado a la configuración del sitiuo web, lo más importante en la configuración e la parte inicial `ALLOWED_HOSTS = []` que indica cuales son las direcciones permitidas para acceder al host ``
DEBUG = True este permite en dev, que entrege más informacion, cuando esté en prod, debe estar en False.

En django, cuando se crea una carpeta, esta se llama proyecto, no app.

Los proyectos, en django, se dividen en distas aplicaciones en el proyecto. un proyecto está conformado en distintas aplicaciones

LAs aplicaciones intaladas por defecto son las siguientes definidas en  `firt_web/setting.py`:
```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Tambien más aabjo, se define la base de datos

```python

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

acá como es un string, se puede definir cualquier otro formato de base de datos.

Tambien está la forma de definir los archivos estaticos, es decir que django consume para la pagina web, como imagenes, css y JavaScript:
```python
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
```


`first_web/urls.py` Acá se definen las urls que los clientes pueden acceder y tocar, como `home/contact` y cosas por el estilo

esto es para servir contenido
`first_web/wsgi.py`
`first_web/asgi.py`

django, es para crear el contenido y no para servirlo. estos modulos, son para servirlos. por lo cual no es preocupación.

## Aplicaciones en DJango


Se mencionó que django funciona como un proyecto, que posee varias aplicaiones, es por ello que tiene un comando para crear aplicaciones de forma rapida con `python manage.py startapp <name-app>` esto creará una carpeta con el nombre de la app a crear
 
cada carpeta tiene sus propios archivos con la funcionalidad de la aplicación las cuales se van a acoplar al proyecto.

depues estos archivos se llamarán desde el proyecto principal que en este caso es `first_web`. La primer carpeta que se creo, que es el nucleo de la aplicacioin, acá están las configuraciones globales etc.

como el proyecto inicial, no las conoce, se pueden eliminar. No se conectan automaticamente.

### primera app

`python manage.py startapp first_app`, para crear la primera aplicacion del proyecto.

`first_app`, es solo una parte del proyecto.

`first_app/views.py` este es el archivo principal, porque acá se define que se quiere enviar o que se quiere mostrar al cliente o al navegador, para que lo vea en pantalla. acá se muestran los archivos `html`. el archivo `__init__.py` que define que esta carpeta `first_app` es un modulo de python.

tambien existe acá una carpeta llamada `first_app/migrations`. qie solo tien eel archivo init, este solo se tocará cuando toquemos la base de datos.

nosotros en django, no usaremos sql. se utiliza  un modulo que se llama `orm`. que permite interactuar con la base de datos usando python.

sin embargo, para operaciones complejas se puede usar sql.

el archivo `admin.py` acá está el panel de control de la aplicacion. este es un panel que se acrea a partir de aqui

el file `apps.py`  es para darle una cofiguración a la aplicacion 

`model.py` acá es para crear las clases, que se cerarán en tablas de sql. 

el archivo de test.py sirve para crear pruebas a los datos de la bd, y aplicar diferentes lógicas.

como si se ejecutó un buen dato, se lanzo bien la funcion etc.

## Hola mundo 41:30

funcion de python 