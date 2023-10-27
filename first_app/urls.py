from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),# reemplazo por index
    path('about/', views.about),
    # Esto es una ruta con parametros, acá además se 
    # define que esta variable es un string
    path('hello/<str:username>', views.hello),
    path('projects/', views.projects),
    # path('tasks/<int:id>', views.tasks), # se desactivo el parametro
    path('tasks/', views.tasks)
    
]