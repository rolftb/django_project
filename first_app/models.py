from django.db import models

# Create your models here.
class Project(models.Model):
    """
    Esta clase herada de models.Model, 
    lo que implica que esta clase se va a convertir en una tabla 
    de la base de datos.

    Dentro de está clase voy a definir atributos, que se van a 
    convertir en campos de la tabla de la base de datos.
    """
    name = models.CharField(max_length=100)

class Task(models.Model):
    """
    A model representing a task in a project.

    Attributes:
    -----------
    title : str
        The title of the task.
    description : str
        The description of the task.
    project : Project
        The project that the task belongs to.

    """
    title = models.CharField(max_length=100) # titulo de la tarea
    description = models.TextField() # descripción de la tarea, 
    #este puede ser un texto más largo, acá son textos, más largos, 
    # como para escribir un parrafo.
    
    # Acá se busca definir la tarea a un proyecto de verdad
    project = models.ForeignKey(Project, on_delete=models.CASCADE) 
    """
    acá se define la relación entre las tablas, 
    en este caso se define que una tarea pertenece 
    a un proyecto, y que si se elimina el proyecto, 
    se elimina la tarea.
    """