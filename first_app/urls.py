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
