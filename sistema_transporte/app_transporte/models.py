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
        ('GT', 'Gerente de transporte')

    ]
    puesto = models.CharField(
        max_length=2,
        choices=PUESTOS_DISPONIBLES,
        default='CH',
    )

class Vehiculos(models.Model):
    marca   = models.CharField(max_length=20)
    modelo  = models.CharField(max_length=20)

    ESTADOS = [
        ('Di', 'Disponible'),
        ('Em', 'En mantenimiento'),
        ('Et', 'En transporte'),
    ]
    estado  = models.CharField(
        max_length=2,
        choices=ESTADOS,
        default='Di'
    )
