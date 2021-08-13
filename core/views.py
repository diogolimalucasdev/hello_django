from django.shortcuts import render, HttpResponse


# Create your views here.

def hello(request, nome, idade):
    return HttpResponse(f"<h1> hello {nome} com idade de {idade} anos </h1> ")
