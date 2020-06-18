from django.db import models
from django.utils import timezone
import datetime


class Empleados(models.Model):
    nombres = models.CharField(max_length=40)
    apellido_materno = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
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
	marca = models.CharField(max_length=20)
	modelo = models.CharField(max_length=20)
	disponible = models.BooleanField()
	
	def __str__(self):
		return self.marca + ' ' + self.modelo

class Clientes(models.Model):
	nombre_titular = models.CharField(max_length=40)
	numero_tarjeta = models.CharField(max_length=40)
	codigo_seguridad = models.IntegerField()
	correo = models.CharField(max_length=40)
	fecha_vencimiento = models.DateField()

	def __str__(self):
		return self.nombre_titular

class Servicios(models.Model):
	chofer = models.ForeignKey(Empleados, on_delete=models.CASCADE)
	vehiculo = models.ForeignKey(Vehiculos, on_delete=models.CASCADE)
	cliente = models.OneToOneField(Clientes, on_delete=models.CASCADE)
	mascota = models.CharField(max_length=40)
	lugar_inicio = models.CharField(max_length=40)
	lugar_destino = models.CharField(max_length=40)

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
	cve_detalle_venta = models.IntegerField(default=0)

	def __str__(self):
	    return 'Masctota '+self.mascota

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
	servicio = models.OneToOneField(Servicios, on_delete=models.CASCADE)
	fecha_inicio = models.DateField()
	fecha_limite = models.DateField()
	horario_inicio = models.TimeField(choices=HORAS)
	horario_fin = models.TimeField(choices=HORAS)

	objects = models.Manager()

	def __str__(self):
	    return str(self.fecha_inicio)

class Catalago(models.Model):
	vehiculo = models.ForeignKey(Vehiculos, on_delete=models.CASCADE)
	precio = models.FloatField()
	descripcion = models.CharField(max_length=50)
	url = models.CharField(max_length=100)

	objects = models.Manager()

	def __str__(self):
	    return self.descripcion
