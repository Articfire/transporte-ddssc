# from django.shortcuts import render
from django.http import HttpResponse
from .models import Empleados, Vehiculos, Checklist, Servicios
# import requests
import json

def index(request):
    return HttpResponse('Bienvenid@ al inicio!')