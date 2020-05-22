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
        ('DI', 'Disponible'),
        ('NO', 'No Disponible')]
    estado = models.CharField(
        max_length=2,
        choices=ESTADOS_DEl_VEHICULO,
        default='DI')

class Clientes(models.Model):
    nombres          = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    telefono         = models.CharField(max_length=20)
    correo           = models.CharField(max_length=30)
    clave            = models.CharField(max_length=20)

class Pagos(models.Model):
    nombre_titular   = models.CharField(max_length=20)
    numero_tarjeta   = models.CharField(max_length=40)
    fecha_expiracion = models.DateField(auto_now=False, auto_now_add=False)
    codigo_seguridad = models.IntegerField()

class Servicios(models.Model):
    lugar_inicio  = models.CharField(max_length=50)
    lugar_destino = models.CharField(max_length=50)
    fecha         = models.DateTimeField()
    a_transportar = models.CharField(max_length=50)
    chofer        = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    vehiculo      = models.ForeignKey(Vehiculos, on_delete=models.CASCADE)
    solicitante   = models.OneToOneField(Clientes, on_delete=models.CASCADE)
    pago          = models.OneToOneField(Pagos, on_delete=models.CASCADE)

    ESTADOS_DEL_SERVICIO = [
        ('SS', 'Servicio Solicitado')
        ('PH', 'Por hacer'),
        ('EP', 'En proceso'),
        ('TE', 'Terminado'),
        ('FI', 'Firmado'),]
    estado        = models.CharField(
        choices=ESTADOS_DEL_SERVICIO, 
        max_length=2, 
        default='PH')
