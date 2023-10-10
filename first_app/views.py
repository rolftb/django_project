from django.shortcuts import render
from django.http import HttpResponse

# view llamada Index que no recibe parametros
def index(request):
    return HttpResponse("<h1>Index</h1>")
# view llamada Hello que recibe un parametro y lo imprime
def hello(request, username:str):
    print(username)
    return HttpResponse("<h1>Hello world</h1>")
def about(request):
    return HttpResponse("<h1>About</h1>")