# pylint: disable=E1101
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from .models import Empleados, Vehiculos, Clientes, Pagos, Servicios, Agenda, Catalago
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
        catalago_id = request.POST.get('catalago_id')
        request.session['catalago_id'] = int(catalago_id)
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
            fecha_servicio = request.POST.get('fecha_servicio')

            if request.POST.get('hora_servicio'):
                hora = datetime.datetime.strptime(request.POST.get('hora_servicio'), '%H:%M:%S').time()

                request.session['fecha_inicio'] = fecha_servicio,
                request.session['fecha_limite'] = fecha_servicio,
                request.session['horario_inicio'] = str(hora),
                request.session['horario_fin'] = str(datetime.time(hora.hour+1, hora.minute, hora.second))
                return HttpResponseRedirect('pago')
            else:
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
    data = {}
    try:
        if request.method == 'POST':
            numero_tarjeta = request.POST['numero_tarjeta']
            fecha_expiracion = request.POST['fecha_expiracion']
            codigo_seguridad = int(request.POST['codigo_seguridad'])
            pago_nuevo = Pagos(
                numero_tarjeta=numero_tarjeta,
                codigo_seguridad=codigo_seguridad,
                fecha_vencimiento=fecha_expiracion,
            )
            pago_nuevo.save()

            request.session['pago_id'] = pago_nuevo.id

            return HttpResponseRedirect('notificacion')
        return render(request, "pago.html", data)
    except Exception as e:
        return HttpResponse('Error: '+str(e))

def notificacion(request):
    data = {'disponible': True}
    citas = Agenda.objects.all()

    fecha = datetime.datetime.strptime(request.session['fecha_inicio'][0], '%Y-%m-%d').date()
    hora = datetime.datetime.strptime(request.session['horario_inicio'][0], '%H:%M:%S').time()

    if request.method == 'POST':
        if request.POST.get('aceptar'):
            nueva_cita = Agenda(
                fecha_inicio=fecha,
                fecha_limite=fecha,
                horario_inicio=hora,
                horario_fin=datetime.time(
                    hour=hora.hour+1, 
                    minute=hora.minute, 
                    second=hora.second
                )
            )
            nueva_cita.save()
            request.session['agenda_id'] = nueva_cita.id

            catalago = Catalago.objects.get(id=request.session['catalago_id'])
            vehiculo = Vehiculos.objects.get(id=catalago.vehiculo_id)
            cliente = Clientes.objects.get(id=request.session['cliente_id']),
            pago = Pagos.objects.get(id=request.session['pago_id']),

            nuevo_servicio = Servicios(
                chofer=Empleados.objects.get(nombres='Juan Pablo'),
                vehiculo=vehiculo,
                cliente=cliente[0],
                pago=pago[0],
                servicio_vendido=catalago,
                cita=nueva_cita,
                monto_pagado=catalago.precio,
                mascota=request.session['mascota'],
                lugar_inicio=request.session['lugar_inicio'],
                lugar_destino=request.session['lugar_destino']
            )
            nuevo_servicio.save()

            return HttpResponseRedirect('asignacion')
        else:
            return HttpResponseRedirect('agenda')
    for cita in citas:
        if cita.fecha_inicio == fecha and cita.horario_inicio == hora:
            data['disponible'] = False
    return render(request, 'notificacion.html', data)

def asignacion(request):
    if request.method == 'POST':
        servicio_id = request.POST.get('servicio')
        servicio = Servicios.objects.get(id=servicio_id)
        servicio.estado = 'TE'
        servicio.chofer = Empleados.objects.get(nombres=request.POST.get('chofer'))
        servicio.vehiculo = Vehiculos.objects.get(modelo=request.POST.get('vehiculo')[-1::])
        servicio.save()
        return HttpResponseRedirect('firma/'+str(servicio_id))
    data = {'servicios': []}
    servicios = Servicios.objects.all()
    for servicio in servicios:
        cita = Agenda.objects.get(id=servicio.cita.id)
        data['servicios'].append({
            'id': servicio.id,
            'mascota': servicio.mascota,
            'lugar_inicio': servicio.lugar_inicio,
            'lugar_destino': servicio.lugar_destino,
            'fecha_inicio': str(cita.fecha_inicio),
            'fecha_limite': str(cita.fecha_limite),
            'horario_inicio': str(cita.horario_inicio),
            'horario_fin': str(cita.horario_fin),
        })
        data.update({
            'choferes': Empleados.objects.filter(puesto='CH'),
            'vehiculos': Vehiculos.objects.all()
        })

    return render(request, 'asignacion.html', data)

def firma(request, servicio_id):
    servicio = Servicios.objects.get(id=servicio_id)
    if servicio.estado == 'FI':
        data = {'firmado': True}
    else:
        data = {'firmado': False}
    if request.method == 'POST' and request.POST.get('firma'):
        servicio.estado = 'FI'
        servicio.save()
        return HttpResponseRedirect(str(servicio_id))
    data.update({
        'chofer': servicio.chofer,
        'vehiculo': servicio.vehiculo,
    })
    return render(request, 'firma.html', data)

def api_documentacion(request):
    return render(request, 'api_documentacion.html')

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
                lista_horas = utils.calcular_lista_horas(articulo.horario_inicio, articulo.horario_inicio)
                fecha['horas'] = [
                    str(datetime.time(indice, 0)) 
                    for indice in range(9, 18) 
                    if str(datetime.time(indice, 0)) not in lista_horas
                ]


    return HttpResponse(json.dumps({'disponibilidad': data}, sort_keys=False, indent=4), content_type="application/json")

@csrf_exempt
def consumir_venta(request, detalle_venta_id):
    try:
        if request.method == 'POST':
            base_url = 'https://apimascotasventas.azurewebsites.net/api/'
            
            res_detalle_ventas = requests.get(base_url+'DetalleVentas/'+ str(detalle_venta_id))
            res_detalle_ventas = res_detalle_ventas.json()
            
            fecha_agendada = res_detalle_ventas['fecha_agendada']
            hora_agendada = res_detalle_ventas['hora_agendada']
            cve_servicio = res_detalle_ventas['cve_servicio']
            cve_cliente = res_detalle_ventas['Venta']['cve_cliente']

            res_clientes = requests.get(base_url+'Clientes/'+ str(cve_cliente))
            res_clientes = res_clientes.json()

            nombre_tarjeta = res_clientes['nombre_tarjeta']
            numero_tarjeta = res_clientes['numero_tarjeta']
            cvv_tarjeta = res_clientes['cvv_tarjeta']
            correo = res_clientes['correo']
            anio_vencimiento = res_clientes['anio_vencimiento']
            mes_vencimiento = res_clientes['mes_vencimiento']

            empleado = Empleados.objects.get(nombres="Chofer")

            catalago = Catalago.objects.get(id=int(cve_servicio))

            vehiculo = Vehiculos.objects.get(id=int(catalago.vehiculo_id))

            cliente = Clientes(nombre_titular=nombre_tarjeta, correo=correo)
            cliente.save()

            pago = Pagos(
                numero_tarjeta=numero_tarjeta,
                codigo_seguridad=int(cvv_tarjeta),
                fecha_vencimiento=datetime.date(year=int(anio_vencimiento), month=int(mes_vencimiento), day=1)
            )
            pago.save()
            
            hora_agendada = datetime.datetime.strptime(hora_agendada, '%H:%M:%S').time()
            agenda = Agenda(
                fecha_inicio=datetime.datetime.strptime(fecha_agendada, '%Y-%m-%d').date(),
                fecha_limite=datetime.datetime.strptime(fecha_agendada, '%Y-%m-%d').date(),
                horario_inicio=hora_agendada,
                horario_fin=datetime.time(hour=hora_agendada.hour+1, minute=hora_agendada.minute, second=hora_agendada.second)
            )
            agenda.save()

            servicio = Servicios(
                chofer_id=empleado.id,
                vehiculo_id=vehiculo.id,
                cliente_id=cliente.id,
                pago_id=pago.id,
                servicio_vendido=catalago,
                cita=agenda,
                mascota="Mascota",
                lugar_inicio="Lugar de origen",
                lugar_destino="Lugar de destino",
                departamento_venta="ventas",
                monto_pagado=catalago.precio
            )
            servicio.save()

            return HttpResponse("Peticion exitosa. El Id enviado fue "+str(detalle_venta_id)+".")
        else:
            return HttpResponse("El metodo de la peticion Http debe de ser POST.")
    except Exception as e:
        print("Error en "+str(e))
        return HttpResponse("Error: {}".format(e))
