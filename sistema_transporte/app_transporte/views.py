# pylint: disable=E1101
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from .models import Agenda, Servicios, Clientes, Catalago
from . import utilerias as utils

import datetime
import requests
import json


def solicitud_transporte(request):
    data = {}
    if request.method == 'POST':
        try:
            nombre_titular = request.POST['nombre_titular']
            correo = request.POST['correo']

            c = Clientes(nombre_titular=nombre_titular, correo=correo)
            c.save()

            request.session['cliente_id'] = c.id
            request.session['mascota'] = request.POST['mascota']
            request.session['lugar_inicio'] = request.POST['lugar_inicio']
            request.session['lugar_destino'] = request.POST['lugar_destino']

            return HttpResponseRedirect('catalago')
        except Exception as e:
            return HttpResponse('Error: {}'.format(e))
    return render(request, 'solicitud_transporte.html', data)

def catalago(request):
    data = {}
    if request.method == 'POST':
        catalago_id = int(request.POST['catalago_id'])
        request.session['catalago_id'] = catalago_id
        return HttpResponseRedirect('agenda')
    catalago = list(Catalago.objects.all())
    data = {'catalago': catalago}
    return render(request, 'catalago.html', data)

def agenda(request):
    try:
        data = {}
        disponibilidad = requests.get('http://localhost:8000/api/disponibilidad').json()
        data.update(disponibilidad)
        if request.method == 'POST':
            # buscar objeto mediante fecha
            fecha_servicio = request.POST['fecha_servicio']
            for objeto in data['disponibilidad']:
                if fecha_servicio == objeto['fecha']:
                    data.update({
                        'objeto': objeto
                    })
                    break
    except Exception as e:
        return HttpResponse("Error: {}".format(e))
    return render(request, 'agenda.html', data)

def pago(request):
    return HttpResponse("Pago")

def notificacion(request):
    data = {}
    return render(request, 'notificacion.html', data)

def asignacion(request):
    data = {}
    return render(request, 'asignacion.html', data)

def firma(request):
    data = {}
    return render(request, 'firma.html', data)

def api_documentacion(request):
    data = {}
    return render(request, 'api_documentacion.html', data)

def api_catalago_filtro(request, catalago_id):
    try:
        articulo = Catalago.objects.get(id=catalago_id)
        data = {
            'id': articulo.id,
            'descripcion': articulo.descripcion,
            'precio': articulo.precio,
            'url': articulo.url,
            'marca_vehiculo': articulo.vehiculo.marca,
            'modelo_vehiculo': articulo.vehiculo.modelo
        }
    except Exception:
        data = {'error': 'Ese id no apunta a ningun articulo del catalago.'}
    return HttpResponse(json.dumps(data, sort_keys=False, indent=4), content_type="application/json")

def api_catalago(request):
    data = []
    catalago = Catalago.objects.all()
    for articulo in catalago:
        data.append({
            'id': articulo.id,
            'descripcion': articulo.descripcion,
            'precio': articulo.precio,
            'url': articulo.url,
            'marca_vehiculo': articulo.vehiculo.marca,
            'modelo_vehiculo': articulo.vehiculo.modelo
        })
    return HttpResponse(json.dumps(data, sort_keys=False, indent=4), content_type="application/json")

def api_disponibilidad(request):
    agenda = Agenda.objects.all()
    hoy = datetime.date.today()
    data = []

    # Lista de fechas que abarcan desde el dia actual hasta el fin del mes
    fechas_mes = [datetime.date(year=hoy.year, month=hoy.month, day=indice) for indice in range(hoy.day, 31)]

    for fecha_mes in fechas_mes:
        data.append({
            'fecha': str(fecha_mes),
            'horas': [str(datetime.time(indice, 0)) for indice in range(9, 18)]
        })
    
    for articulo in agenda:
        fechas_ocupadas = [
            str(articulo.fecha_inicio + datetime.timedelta(days=x))
            for x in range((articulo.fecha_limite - articulo.fecha_inicio).days + 1)
        ]
        for fecha in data:
            if fecha['fecha'] in fechas_ocupadas:
                lista_horas = utils.calcular_lista_horas(articulo.horario_inicio, articulo.horario_fin)
                fecha['horas'] = [
                    str(datetime.time(indice, 0)) 
                    for indice in range(9, 18) 
                    if str(datetime.time(indice, 0)) not in lista_horas
                ]


    return HttpResponse(json.dumps({'disponibilidad': data}, sort_keys=False, indent=4), content_type="application/json")

@csrf_exempt
def api_venta(request, detalle_venta_id):
    if request.method == 'POST':
        # print("ID: {}".format(detalle_venta_id))
        
        return HttpResponse("Peticion exitosa. El Id enviado fue {}.".format(detalle_venta_id))
    else:
        return HttpResponse("El metodo de la peticion Http debe de ser POST.")

@csrf_exempt
def api_reservacion(request):
    if request.method == 'POST':
        pass
