# Generated by Django 3.0.7 on 2020-06-23 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_transporte', '0036_auto_20200621_1414'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='agenda',
        #     name='servicio',
        # ),
        migrations.RemoveField(
            model_name='servicios',
            name='cve_detalle_venta',
        ),
        migrations.AddField(
            model_name='servicios',
            name='cita',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='app_transporte.Agenda'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicios',
            name='departamento_venta',
            field=models.CharField(default='ventas', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicios',
            name='monto_pagado',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicios',
            name='servicio_vendido',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app_transporte.Catalago'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='catalago',
            name='descripcion',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='empleados',
            name='apellido_materno',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='empleados',
            name='apellido_paterno',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='servicios',
            name='mascota',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='vehiculos',
            name='marca',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='vehiculos',
            name='modelo',
            field=models.CharField(max_length=40),
        ),
    ]