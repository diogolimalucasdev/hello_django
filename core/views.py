from django.shortcuts import render, HttpResponse


# Create your views here.

def hello(request, nome, idade):
    return HttpResponse(f"<h1> hello {nome} com idade de {idade} anos </h1> ")


def soma(request, numero1, numero2):
    return HttpResponse(f"{numero1} + {numero2} = {numero1 + numero2}")
