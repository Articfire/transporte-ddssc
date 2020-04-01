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

    def __str__(self):
        print(self.apellido_paterno+" "+self.nombres)

class Vehiculos(models.Model):
    marca  = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)

    ESTADOS_DEl_VEHICULO = [
        ('DI', 'Disponible'),
        ('NO', 'No Disponible')]
    estado = models.CharField(
        max_length=2,
        choices=ESTADOS_DEl_VEHICULO,
        default='DI')

    def __str__(self):
        print(self.marca+" "+self.modelo)

class Checklist(models.Model):
    chofer   = models.OneToOneField(Empleados, on_delete=models.CASCADE)
    vehiculo = models.OneToOneField(Vehiculos, on_delete=models.CASCADE)

    def __str__(self):
        print("Agenda de "+Empleados.objects.get(id=self.chofer)+", conductor del "+Vehiculos.objects.get(id=self.vehiculo))

class Servicios(models.Model):
    checklist     = models.ForeignKey(Checklist, on_delete=models.CASCADE)
    lugar_inicio  = models.CharField(max_length=50)
    lugar_destino = models.CharField(max_length=50)
    fecha_inicio  = models.DateTimeField()
    descripcion   = models.CharField(max_length=50)

    ESTADOS_DEL_SERVICIO = [
        ('PH', 'Por hacer'),
        ('EP', 'En proceso'),
        ('TE', 'Terminado'),
        ('FI', 'Firmado'),
        ('PR', 'Problema')]
    estado        = models.CharField(
        choices=ESTADOS_DEL_SERVICIO, 
        max_length=2, 
        default='PH')

    def __str__(self):
        print(self.descripcion)


# class LlavesLiberacion(models.Model):
#     llave_liberacion = models.CharField(max_length=20)
#     servicio = models.OneToOneField(Servicios, on_delete=models.CASCADE)


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