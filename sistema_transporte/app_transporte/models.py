from django.db import models
from django.utils import timezone


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
			('GT', 'Gerente de transporte')
		],
        default='CH'
	)

class Vehiculos(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    disponible = models.BooleanField()

class Clientes(models.Model):
    nombres = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    correo = models.CharField(max_length=30)

class Pagos(models.Model):
    nombre_titular = models.CharField(max_length=20)
    numero_tarjeta = models.CharField(max_length=20)
    fecha_expiracion = models.DateField(auto_now=False, auto_now_add=False)
    codigo_seguridad = models.IntegerField()

class Servicios(models.Model):
	chofer = models.ForeignKey(Empleados, on_delete=models.CASCADE)
	vehiculo = models.ForeignKey(Vehiculos, on_delete=models.CASCADE)
	cliente = models.OneToOneField(Clientes, on_delete=models.CASCADE)
	pago = models.OneToOneField(Pagos, on_delete=models.CASCADE)
	mascota = models.CharField(max_length=20)
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

class Agenda(models.Model):
	servicio = models.OneToOneField(Servicios, on_delete=models.CASCADE)
	fecha_inicio = models.DateTimeField()
	fecha_limite = models.DateTimeField()