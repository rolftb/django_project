# Pasos pobre el curso de DJango

[Django, Curso de Django para Principiantes](https://youtu.be/T1intZyhXDU?si=7CSKC-P6NlzA1foN)

## Iniciar el ambiente

Extensiones a instalar:

- python
- Material Icon Theme, este sirve para identificar los archivos del proyecto y diferenciarlos
- After Dark, es uitilizado para cambiar el color de visualizador de código

### Create a env**

para installar `virtualenv` que es usado para crear ambientes virtuales
`pip install virtualenv`

con esto se crea el ambiente `virtualenv venv` ahora se debe acceder al ambiente con  windows: `./venv/Scrips/activate.bat` MAC: `source venv/bin/activate`

luego para alinear el interprete (VScode) se pone en el buscador `>select interprete` y se selecciona el ambiente creado (recomendado por VScode)

Luego se realiza el `pip install django`

se puede revisar la version utilizando `python -m django-admin -version` o iniciando python y utilizando `django.get_version()`, luego de `python import django`

`django-admin startproject <nombre-del-proyecto>`
esto crea el sitio de django, con todos los archivos. Acá se créa el poryecto nuevo, el adminisatrador de proeycto.

En este caso, como ya tenemos una carpeta ya creada, entonces se creará el pryecto, en la carpeta actual sin crear una nueva carpeta dentro de la actual. para ello se utiliza el comando `django-admin startproject <nombre-del-proyecto> .` el punto luego del nombre del proyecto indica que creará todo desde el directorio actual. `django-admin startproject first_web .`

### Ejecución

al realizar el comando `django-admin startproject first_web .`
se crean varios archivos, el archivo inicial `manage.py` es utilizado para lanzar el webapp, para ello se puede lanzar con el siguiente comando: `python manage.py runserver`

al ejecutar el servidor se crea el archivo `db.sqite3` que es donde se aloja la base de datos

ahora pude que tengamos corriendo más de una web app, por ello se puede definir el puerto asi `python manage.py runserver 3000` se definión el purto `3000`

### Estructura del proyecto

`manage.py` es utilizada para ejecutar programas administratuivos, como anteriormente se mostró que sirvió para montar un servidor `python manage.py runserver 3000`

al ejecutar el comando `python manage.py --help` muestra todo los comandos que este archivo posee, para lanzar nuevas cosas, como montar un servidor, crear nuevos usuarios administrativos (`createsuperuser`)etc.

`db.sqlite3` es la base de datos utilizada en desarrollo, para el paso a prod, se debe realizar un cambio y definir algo más formal. pero django se hace cargo de ese cambio.

#### mysite (`./mysite`) o carpeta "firt_webb"

El archivo `__init__.py`, indica que la carpeta es un modulo de python, este archivo viene vacio

`first_web/settings.py` esta asociado a la configuración del sitiuo web, lo más importante en la configuración e la parte inicial `ALLOWED_HOSTS = []` que indica cuales son las direcciones permitidas para acceder al host ``
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

### Aplicaciones en DJango

Se mencionó que django funciona como un proyecto, que posee varias aplicaiones, es por ello que tiene un comando para crear aplicaciones de forma rapida con `python manage.py startapp <name-app>` esto creará una carpeta con el nombre de la app a crear

cada carpeta tiene sus propios archivos con la funcionalidad de la aplicación las cuales se van a acoplar al proyecto.

depues estos archivos se llamarán desde el proyecto principal que en este caso es `first_web`. La primer carpeta que se creo, que es el nucleo de la aplicacioin, acá están las configuraciones globales etc.

como el proyecto inicial, no las conoce, se pueden eliminar. No se conectan automaticamente.

#### primera app

`python manage.py startapp first_app`, para crear la primera aplicacion del proyecto.

`first_app`, es solo una parte del proyecto.

`first_app/views.py` este es el archivo principal, porque acá se define que se quiere enviar o que se quiere mostrar al cliente o al navegador, para que lo vea en pantalla. acá se muestran los archivos `html`. el archivo `__init__.py` que define que esta carpeta `first_app` es un modulo de python.

tambien existe acá una carpeta llamada `first_app/migrations`. qie solo tien eel archivo init, este solo se tocará cuando toquemos la base de datos.

nosotros en django, no usaremos sql. se utiliza  un modulo que se llama `orm`. que permite interactuar con la base de datos usando python.

sin embargo, para operaciones complejas se puede usar sql.

- el archivo `admin.py` acá está el panel de control de la aplicacion. este es un panel que se acrea a partir de aqui
- el file `apps.py`  es para darle una cofiguración a la aplicacion
- `model.py` acá es para crear las clases, que se cerarán en tablas de sql. acá se crean las clases que se crearan en la base de datos.
- el archivo de `test.py` sirve para crear pruebas a los datos de la bd, y aplicar diferentes lógicas. Como si se ejecutó un buen dato, se lanzo bien la funcion etc.

### Hola mundo 41:30

Dentro de la carpeta `first_app` se crea un archivo llamado `views.py` en este archivo se construye la vista, que es lo que se va a mostrar en pantalla.

```python
from django.shortcuts import render
#importar  el hhttp response
from django.http import HttpResponse

# Create your views here.
def hello(request):
    # acá se construye una respuesta http. entonces acña se puede contruir una respuesta http
    return HttpResponse("Hello world")
    # con esto se puede ver en el navegador la respuesta http
``` 

acá se construye una respueta Http, que es lo que se va a mostrar en pantalla. para ello se importa el modulo `HttpResponse` de django.

luego para que está respuests se vizualice en la pagina web hay que asignarle una url, para ello se debe ir al archivo `first_web/urls.py` y se debe definir la nueva ruta asociada a la vista creada en `first_app/views.py`

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    # acá se define la nueva ruta, como no tiene especificado el nombre del dominio, entonces se deja vacio y redirigue al inicio de la pagina.
    path('', views.hello, name='hello'),
]
```
acá se puede complejisar el uso de las urls, para ello se crear en la carpeta `first_app` un archivo llamado `urls.py` y se define la ruta que se quiere utilizar.

```python
# se exporta una lista nueva 
urlpatterns = [
    # se define la ruta que se quiere utilizar
    path('', views.hello, name='hello'),
]
```

acá está lista tendrá la misma lista que se implementa en `urls.py` de `first_web`.

entonces las vista que estában en el modulo principal se deben importar al modulo de la app, para ello se debe importar el modulo `views.py` de la app `first_app` en el modulo `urls.py` de `first_web`

```python
# importa la funcion path
from django.urls import path
# importa las vistas de la app
# from  first_app import views
# como estoy en la carpeta first_app 
# no es necesario poner el nombre de la carpeta
from . import views

urlpatterns = [
        path('', 
        views.hello, # 
        # nombre de la vista, 
        # es utilizado para referenciarla en el template
        name='hello'
        ),
    path('about/',
         views.about,
         )
]
```

Entonces nueto archivo `urls.py` de firt_app, quedará de la siguiente forma:

```python
from django.contrib import admin
from django.urls import (
    path, # funcion que define una ruta
    include, # funcion que incluye las urls de una app
) 

urlpatterns = [
    path('admin/', admin.site.urls),
    # incluye las urls de la app first_app
    path('', include('first_app.urls')),
]
```

acá ademas se puede modificar el path que incluye las urls de la app, para que no se tenga que escribir la ruta completa.

```python
from django.contrib import admin
from django.urls import (
    path, # funcion que define una ruta
    include, # funcion que incluye las urls de una app
) 

urlpatterns = [
    path('admin/', admin.site.urls),
    # Incluye las urls de la app first_app
    path('first_app/', # Esto es un prefijo, que se incorpora antes de las urls que yo defino en first_app
         include('first_app.urls')),
]
```

Ahora todas las urls, que están en `firts_app/urls.py` se deben modificar, para que se incorpore el prefijo `first_app/` antes de cada ruta.

## DATABASE MODELS Django 52:25

Revision de la base de datos

cuando se ejecura la app se puede ejecutar  el compando `python manage.py migrate` para aplicar alog 
(`Runt 'python manage.py migrate' to apply them.`) este comando se encarga de crear las tablas en la base de datos, que se crearon en el archivo `models.py` de la app `first_app`

Al ejecutar el comando `python manage.py runserver` sin realizar el paso recomendado, tendremos el siguiente error:

```zsh
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
October 09, 2023 - 23:34:59
Django version 4.2.5, using settings 'first_web.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

las `migration(s)` son los cambios que se han realizado en la base de datos, y que no se han aplicado. para ello se debe ejecutar el comando `python manage.py migrate` para aplicar los cambios. En base de datos las migraciones son una forma de realizar cambios en la base de datos, sin tener que eliminar la base de datos y crearla de nuevo.

el scrip, de `manage.py` es el que se encarga de crear la base de datos, y de aplicar los cambios en la base de datos. acá uno puede utilizar esto para actualizar la base de datos

Si se ejecuta `pythn manage.py makemigrations` antes de crear la base de datos con `python manage.py migrate` saldrá un mensaje informado que no hay cambios que aplicar. (`No changes detected`).

Se muestra una serie de mensajes, que im pklica que se están creando las tablas dentro de la base de datos.

```zsh
(venv) (base) a4657925@MFH71416CPW web_app_jango % python manage.py migrate  
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
  ````

Para vizualizar las tablas y la base de datos, se puede utilizar el programa 
`DB Browser for SQLite` este programa permite vizualizar la base de datos, y las tablas que se crearon.

Además de construir las tablas dentro de la base de datos, se creo una nueva carpeta llamda `migration` dentro de la carpeta `first_app` y dentro de esta carpeta se creó el archivo `__init__.py`

Dentro de las tablas creadas por Django, están las tablas asociadas a los usuarios como `auth_user`, la cual posee campos como `id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`. Estas tablas son creadas por defecto por Django. E incluso Django tiene funciones, para guardar nuevos usuarios, y para validar usuarios. por lo cual no se registran manualmente desde zero.

Puede que nosotros, querramos crear nuevas tablas, para cualquier tipo de proyecto. para esto nosotros tenemos que crear un modelo, que es una clase de python, que se va a convertir en una tabla de la base de datos. Este scrip que esamos ejecutando, se puede ejecutar en cualquier base de datos que nosottros queramos.

### Crear un modelo

Un modelo como se mencionó anteriorme es una clase de python, que se va a convertir en una tabla de la base de datos. para ello se debe crear un archivo llamado `models.py` dentro de la carpeta `first_app` y se debe importar el modulo `models` de django.


Entonces en el archivo `first_app/models.py` se debe crear una clase que herede de `models.Model` y se debe definir los campos que se quieren crear en la tabla de la base de datos.

```python
from django.db import models

# Create your models here.
class Project(models.Model):
    """
    Esta clase herada de models.Model, lo que implica que esta clase se va a convertir en una tabla de la base de datos.

    Dentro de está clase voy a definir atributos, que se van a convertir en campos de la tabla de la base de datos.
    """
    name = models.CharField(max_length=100)
```

Cuando se trabaja con SQL. uno define el tipo de columna. en este caso se define el tipo de columna `CharField` que es un tipo de columna de texto, y se le debe definir el tamaño máximo de la columna, en este caso se define `max_length=100`

Con esto le estoy diciendo que voy a contruir una tabla llamada `Project` y que va a tener un campo llamado `name` que va a ser de tipo `CharField` y que va a tener un tamaño máximo de 100 caracteres.

Si yo ejecuto `python manage.py runserver`, no me aparecerá ningun warning de cambios, es porque aún este modelo no está conectado con el proyecto. 

Para conectarlo, debo ir al archivo `first_web/settings.py` y en la lista `INSTALLED_APPS` debo agregar la app `first_app` que es la que contiene el modelo que se quiere conectar. La lista `INSTALLED_APPS` permite conectar las apps que se crean en el proyecto.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'first_app', # Agrega la app creada
]
```
Un error que me ocurrio fue definir en `first_web/settings.py` la base de datos con otro nombre, entonces al ejecutar el comando `python manage.py makemigrations first_app` me salto el siguiente error:

```zsh
No installed app with label 'first_app'.
```

`python manage.py runserver` no salta ningun problema. Ahora podemos realizar las nuevas migraciones. para ello se debe ejecutar el comando `python manage.py makemigrations`. Este comando lo que hace es buscar todas las clases que heredan de `models.Model` y las convierte en tablas de la base de datos. Este comando puede ser más especifico y se puede ejecutar de la siguiente forma `python manage.py makemigrations first_app` para que solo busque las clases que heredan de `models.Model` en la app `first_app`.

```zsh
(venv) (base) a4657925@MFH71416CPW web_app_jango % python manage.py makemigrations first_app
Migrations for 'first_app':
  first_app/migrations/0001_initial.py
    - Create model Project
```

En este paso se construyó el archivo `0001_initial.py` dentro de la carpeta `first_app/migrations/` este archivo es el que se encarga de crear la tabla en la base de datos.

```python
 name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
```

Acá se vén todas las partes de la tabla creada en `firt_app/models.py` como el nombre de la tabla `Project`, los campos que se crearon `id` y `name` y el tipo de campo `CharField` y el tamaño máximo `max_length=100`.

Esto no se debe tocar, es para tener una referencia de cómo se está creando la tabla en la base de datos.

Ahora si se ejecuta el comando `python manage.py migrate first_app` se aplicarán los cambios en la base de datos.

```zsh
(venv) (base) a4657925@MFH71416CPW web_app_jango % python manage.py migrate first_app
Operations to perform:
  Apply all migrations: first_app
Running migrations:
  Applying first_app.0001_initial... OK
```

Acá se muestra cómo aplicó los cambios en la base de datos indicados en el archivo `0001_initial.py` de la carpeta `first_app/migrations/`.

Ahora creemos, una nueva tabla que almacene las tareas que tiene el usuario

```python

class Task(models.Model):
    title = models.CharField(max_length=100) # titulo de la tarea
    description = models.TextField() # descripción de la tarea, este puede ser un texto más largo, acá son textos, más largos, como para escribir un parrafo.
    
    # Acá se busca definir la tarea a un proyecto de verdad
    project = models.ForeignKey(Project, on_delete=models.CASCADE) # acá se define la relación entre las tablas, en este caso se define que una tarea pertenece a un proyecto, y que si se elimina el proyecto, se elimina la tarea.
```

`ForeignKey` es para definir una relación entre tablas, en este caso se define que una tarea pertenece a un proyecto, y que si se elimina el proyecto, se elimina la tarea. Acá se debe definir el nombre de la tabla, la cual se va a tener una relación. etonces se debe importar la clase `Project` de `first_app/models.py` y se debe definir el tipo de relación, en este caso `on_delete=models.CASCADE` que es para que si se elimina el proyecto, se elimina la tarea.

Ahora qué pasa si yo elimino un proyecto, qué pasa con las tareas asociadasa al proyecto. Para ello se define una nueva opción llamada `on_delete=models.CASCADE` que es para que si se elimina el proyecto, se elimina la tarea. Acá se definió `models.CASCADE`, esta instrucción implica que cuando se elimine un proyecto se eliminen todas las tareas asociadas a ese proyecto.

Ahora se debe aplicar los cambios en la base de datos, para ello se debe ejecutar el comando `python manage.py makemigrations first_app` y luego `python manage.py migrate first_app`

```zsh
(venv) (base) a4657925@MFH71416CPW web_app_jango % python manage.py makemigrations first_app
Migrations for 'first_app':
  first_app/migrations/0002_task.py
    - Create model Task
```

Esto vuelve a crear un archivo `0002_task.py` dentro de la carpeta `first_app/migrations/` este archivo es el que se encarga de crear la tabla en la base de datos.

```python
# Generated by Django 4.2.5 on 2023-10-10 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    # acá indica que esta tabla tiene una dependencia de la tabla Project
    dependencies = [ 
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.project')),
            ],
        ),
    ]
```

Ahora si yo ejecuto `python manage.py migrate` esto ejecutará todas las migraciones


Otra cosa a considerar, si yo desee cambiar el formato de mi base de datos, puedo ir a `firt_web/settings.py` y cambiar el tipo de base de datos, por ejemplo de `sqlite3` a `mysql` o `postgresql` y luego ejecutar el comando `python manage.py migrate` y se aplicarán los cambios en la base de datos.