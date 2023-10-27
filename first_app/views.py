from django.shortcuts import render
from django.http import(
    HttpResponse,
    JsonResponse, # Para retornar un json, esto permite que se pueda usar en una API
    )
# Esto es para poder usar el modelo de la base de datos
from django.shortcuts import get_object_or_404

# Se importan los modelos de la app, para poder usarlos en las vistas
from .models import (Project, Task)

# view llamada Index que no recibe parametros
def index(request):
    # return HttpResponse("<h1>Index</h1>") # reemplazdo por render
    return render(request, 'index.html', {
        'title': 'Index title append',
        'message': 'Hello world',
    })

# view llamada Hello que recibe un parametro y lo imprime
def hello(request, username:str):
    return HttpResponse(f"<h1>Hello {username}</h1>")

def about(request):
    # return HttpResponse("<h1>About</h1>")
    return render(request, "about.html")

# Ahora crearemos una nueva vista llamada projects y otra llamada tasks
def projects(request):
    # projects =list(Project.objects.all().values())
    projects = (Project.objects.all())
    #return HttpResponse("<h1>Projects</h1>") # reemplazdo por render
    # return JsonResponse(projects, safe=False)
    return render(request, "projects.html",
                  {'projects': projects}
                  )

def tasks(request,
          #id:int
          ):
    # Se comenta lo siguiente no se está usando
    # trae la tarea que tenga el id que se le pasa por parametro
    # pero si no existe retorna un error 404
    # task = get_object_or_404(Task, id=id)
    # otro metodo de obtener la tarea
    # task = Task.objects.get(id=id)
      
    # return HttpResponse(f"<h1>Task title: {task.title}</h1>") # reemplazdo por render
    return render(request, "tasks.html")