from django.shortcuts import render
#importar  el hhttp response
from django.http import HttpResponse

# Create your views here.
def hello(request):
    # acá se construye una respuesta http. entonces acña se puede contruir una respuesta http
    
    #return HttpResponse("Hello world") # esto es un formato simple sin html
    # acá se define un formato html
    return HttpResponse("<h1>Hello world</h1>")
    # con esto se puede ver en el navegador la respuesta http
def about(request):
    return HttpResponse("<h1>About</h1>")