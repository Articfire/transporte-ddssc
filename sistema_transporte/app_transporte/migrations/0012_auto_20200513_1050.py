# Generated by Django 3.0.4 on 2020-05-13 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_transporte', '0011_auto_20200506_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicios',
            name='pago',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='app_transporte.Pagos'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicios',
            name='solicitante',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='app_transporte.Clientes'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='servicios',
            name='chofer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_transporte.Empleados'),
        ),
        migrations.AlterField(
            model_name='servicios',
            name='vehiculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_transporte.Vehiculos'),
        ),
    ]
