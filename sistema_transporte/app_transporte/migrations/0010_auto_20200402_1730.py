# Generated by Django 3.0.4 on 2020-04-03 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_transporte', '0009_auto_20200401_1321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicios',
            name='checklist',
        ),
        migrations.AddField(
            model_name='servicios',
            name='chofer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app_transporte.Empleados', verbose_name='Chofer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicios',
            name='vehiculo',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app_transporte.Vehiculos', verbose_name='Vehiculo'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Checklist',
        ),
    ]
