from django.shortcuts import render
from django.http import HttpResponse
# from .models import Empleados, Vehiculos, Checklist, Servicios
# import requests
# import json

def solicitud_transporte(request):
    data = {}
    return render(request, 'solicitud_transporte.html', data)

def pago(request):
    data = {}
    return render(request, 'pago.html', data)

def agenda(request):
    data = {}
    return render(request, 'agenda.html', data)

def asignacion(request):
    data = {}
    return render(request, 'asignacion.html', data)

def firma(request):
    data = {}
    return render(request, 'firma.html', data)