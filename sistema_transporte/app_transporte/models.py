from django.db import models
import datetime


class Empleados(models.Model):
    nombres = models.CharField(max_length=40)
    apellido_materno = models.CharField(max_length=40)
    apellido_paterno = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField()
    rfc = models.CharField(max_length=13)

    puesto = models.CharField(
        max_length=2,
        choices=[
	    ('CH', 'Chofer'),
	    ('TM', 'Tecnico de mantenimiento'),
	    ('SC', 'Supervisor de Chofer'),
	    ('JM', 'Jefe de mantenimiento'),
	    ('GT', 'Gerente de transporte'),
	],
        default='CH'
    )
            
    def __str__(self):
        return self.nombres

class Vehiculos(models.Model):
	marca = models.CharField(max_length=40)
	modelo = models.CharField(max_length=40)
	disponible = models.BooleanField()
	
	def __str__(self):
		return self.marca + ' ' + self.modelo

class Clientes(models.Model):
	nombre_titular = models.CharField(max_length=40)
	correo = models.CharField(max_length=40)

	def __str__(self):
		return self.nombre_titular

class Pagos(models.Model):
	numero_tarjeta = models.CharField(max_length=40)
	codigo_seguridad = models.IntegerField()
	fecha_vencimiento = models.DateField()

	def __str__(self):
		return self.numero_tarjeta

class Agenda(models.Model):
	HORAS = (
		(datetime.time(9, 0), '9 AM'),
		(datetime.time(10, 0), '10 AM'),
		(datetime.time(11, 0), '11 AM'),
		(datetime.time(12, 0), '12 PM'),
		(datetime.time(13, 0), '1 PM'),
		(datetime.time(14, 0), '2 PM'),
		(datetime.time(15, 0), '3 PM'),
		(datetime.time(16, 0), '4 PM'),
		(datetime.time(17, 0), '5 PM'),
	)
	fecha_inicio = models.DateField()
	fecha_limite = models.DateField()
	horario_inicio = models.TimeField(choices=HORAS)
	horario_fin = models.TimeField(choices=HORAS)

	def __str__(self):
	    return str(self.fecha_inicio)

class Catalago(models.Model):
	vehiculo = models.ForeignKey(Vehiculos, on_delete=models.CASCADE)
	precio = models.FloatField()
	descripcion = models.CharField(max_length=40)
	url = models.CharField(max_length=100)

	objects = models.Manager()

	def __str__(self):
	    return self.descripcion

class Servicios(models.Model):
	chofer = models.ForeignKey(Empleados, on_delete=models.CASCADE)
	vehiculo = models.ForeignKey(Vehiculos, on_delete=models.CASCADE)
	cliente = models.OneToOneField(Clientes, on_delete=models.CASCADE)
	pago = models.OneToOneField(Pagos, on_delete=models.CASCADE)
	servicio_vendido = models.ForeignKey(Catalago, on_delete=models.CASCADE)
	cita = models.OneToOneField(Agenda, on_delete=models.CASCADE)

	mascota = models.CharField(max_length=30)
	lugar_inicio = models.CharField(max_length=40)
	lugar_destino = models.CharField(max_length=40)
	departamento_venta = models.CharField(max_length=40)
	monto_pagado = models.FloatField()

	estado = models.CharField(
	    max_length=2,
	    choices=[
            ('SO', 'Solicitado'),
			('AG', 'Agendado'),
			('EJ', 'Ejecucion'),
			('TE', 'Terminado'),
			('FI', 'Firmado')
	    ],
	    default='SO'
	)

	def __str__(self):
	    return "Transporte de "+self.mascota+" a destino "+self.lugar_destino+"."
