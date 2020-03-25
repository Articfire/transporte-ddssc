from django.shortcuts import render
from django.http import HttpResponse
import json

def vistaTexto(request):
    data = {}
    return HttpResponse("Probando")

def vistaTemplate(request, name):
    data = {'nombre':name}
    return render(request, 'index.html', data)