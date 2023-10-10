from django.shortcuts import render
from django.http import(
    HttpResponse,
    JsonResponse, # Para retornar un json, esto permite que se pueda usar en una API
    )
# Se importan los modelos de la app, para poder usarlos en las vistas
from .models import (Project, Task)

# view llamada Index que no recibe parametros
def index(request):
    return HttpResponse("<h1>Index</h1>")
# view llamada Hello que recibe un parametro y lo imprime
def hello(request, username:str):
    return HttpResponse(f"<h1>Hello {username}</h1>")
def about(request):
    return HttpResponse("<h1>About</h1>")

# Ahora crearemos una nueva vista llamada projects y otra llamada tasks
def projects(request):
    projects =list(Project.objects.all().values())
    #return HttpResponse("<h1>Projects</h1>")
    return JsonResponse(projects, safe=False)

def tasks(request,id:int):
    task=Task.objects.get(id=id)
    return HttpResponse(f"<h1>Task title: {task.title}</h1>")
