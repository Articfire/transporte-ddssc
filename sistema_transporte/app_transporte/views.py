from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from datetime import datetime
import json

def solicitud_transporte(request):
    data = {}
    form_data = request.POST.dict()
    if request.method == 'POST':
        nombres_cliente = form_data['nombres-cliente']
        apellido_paterno = form_data['apellido-paterno']
        apellido_materno = form_data['apellido-materno']
        telefono = form_data['telefono']
        correo = form_data['correo']

        lugar_origen = form_data['lugar-origen']
        lugar_destino = form_data['lugar-destino']
        fecha_origen = form_data['fecha-origen']
        fecha = form_data['fecha']
        mascota = form_data['mascota']

        Clientes.objects.create(
            nombres=nombres_cliente,
            apellido_paterno=apellido_paterno,
            apellido_materno=apellido_materno,
            telefono=telefono,
            correo=correo
        )

        request.session['data'] = {
            "lugar_origen" : lugar_origen,
            "lugar_destino" : lugar_destino,
            "fecha_origen" : fecha_origen,
            "fecha" : fecha,
            "mascota" : mascota,
        }

        return HttpResponseRedirect('pago')
    return render(request, 'solicitud_transporte.html', data)

def pago(request):
    data = {}
    form_data = request.POST.dict()
    if request.method == 'POST':
        nombre_titular = form_data['nombre-titular']
        numero_tarjeta = form_data['numero-tarjeta']
        fecha_expiracion = form_data['fecha-expiracion']
        codigo_seguridad = form_data['codigo-seguridad']

        Pagos.objects.create(
            nombre_titular=nombre_titular,
            numero_tarjeta=numero_tarjeta,
            fecha_expiracion=fecha_expiracion,
            codigo_seguridad=codigo_seguridad
        )
        return HttpResponseRedirect('agenda')
    return render(request, 'pago.html', data)

def agenda(request):
    data = {}
    if request.method == 'POST':
        return HttpResponseRedirect('asignacion')
    return render(request, 'agenda.html', data)

def asignacion(request):
    data = {}
    return render(request, 'asignacion.html', data)

def firma(request):
    data = {}
    return render(request, 'firma.html', data)

def api_agenda(request):
    agenda = Agenda.objects.all()
    lista_agenda = []

    for articulo in agenda:
        lista_agenda.append({
            'fecha_origen': str(articulo.fecha_origen),
            'fecha_limite': str(articulo.fecha_limite)
        })
    return HttpResponse(json.dumps(lista_agenda))