from django.db import models
from django.utils import timezone


class Empleados(models.Model):
    nombres          = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    rfc              = models.CharField(max_length=13)

    PUESTOS_DISPONIBLES = [
        ('CH', 'Chofer'),
        ('TM', 'Tecnico de mantenimiento'),
        ('SC', 'Supervisor de Chofer'),
        ('JM', 'Jefe de mantenimiento'),
        ('GT', 'Gerente de transporte')]
    puesto              = models.CharField(
        max_length=2,
        choices=PUESTOS_DISPONIBLES,
        default='CH')

class Vehiculos(models.Model):
    marca  = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)

    ESTADOS_DEl_VEHICULO = [
        ('Di', 'Disponible'),
        ('Ma', 'En mantenimiento'),
        ('Tr', 'En transporte') ]
    estado = models.CharField(
        max_length=2,
        choices=ESTADOS_DEl_VEHICULO,
        default='Di')

class Checklist(models.Model):
    chofer   = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculos, on_delete=models.CASCADE)

class Servicios(models.Model):
    checklist     = models.ForeignKey(Checklist, on_delete=models.CASCADE)
    lugar_inicio  = models.CharField(max_length=50)
    lugar_destino = models.CharField(max_length=50)
    fecha_inicio  = models.DateTimeField()

    ESTADOS_DEL_SERVICIO = [
        ('PH', 'Por hacer'),
        ('EP', 'En proceso'),
        ('Te', 'Terminado'),
        ('Fi', 'Firmado'),
        ('Pr', 'Problema')]
    estado        = models.CharField(
        choices=ESTADOS_DEL_SERVICIO, 
        max_length=2, 
        default='PH')

# class LlavesLiberacion(models.Model):
#     llave_liberacion = models.CharField(max_length=20)
#     servicio = models.ForeignKey(Servicios, on_delete=models.CASCADE)


# Ideas:
# 1.Que haya una tabla llamada "LlavesLiberacion" que
# contenga codigos alfanumericos que el gerente le da 
# al cliente una vez que se registra su solicitud de 
# transporte para que solo el cliente pueda liberar un 
# servicio de transporte desde el sitio web, en el cual 
# habra un campo de texto para que el cliente inserte 
# el token desde su dispositivo.
#
# 2.