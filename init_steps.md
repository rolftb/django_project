# Iniciar el ambiente

**Create a env**
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
