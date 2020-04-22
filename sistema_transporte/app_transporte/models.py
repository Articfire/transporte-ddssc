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

class Servicios(models.Model):
    lugar_inicio  = models.CharField(max_length=50)
    lugar_destino = models.CharField(max_length=50)
    fecha_inicio  = models.DateTimeField()
    descripcion   = models.CharField(max_length=50)
    chofer        = models.ForeignKey(Empleados, verbose_name="Chofer", on_delete=models.CASCADE)
    vehiculo     = models.ForeignKey(Vehiculos, verbose_name="Vehiculo", on_delete=models.CASCADE)

    ESTADOS_DEL_SERVICIO = [
        ('ES', 'En Solicitud'),
        ('SC', 'Solicitud Cancelada')
        ('PH', 'Por hacer'),
        ('EP', 'En proceso'),
        ('TE', 'Terminado'),
        ('FI', 'Firmado'),
    estado        = models.CharField(
        choices=ESTADOS_DEL_SERVICIO, 
        max_length=2, 
        default='PH')

    def __str__(self):
        print(self.descripcion)
