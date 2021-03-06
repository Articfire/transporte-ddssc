# Generated by Django 3.0.4 on 2020-05-06 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_transporte', '0010_auto_20200402_1730'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=20)),
                ('apellido_materno', models.CharField(max_length=20)),
                ('apellido_paterno', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=20)),
                ('correo', models.CharField(max_length=30)),
                ('clave', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pagos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_titular', models.CharField(max_length=20)),
                ('numero_tarjeta', models.CharField(max_length=40)),
                ('fecha_expiracion', models.DateField()),
                ('codigo_seguridad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Solicitudes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lugar_inicio', models.CharField(max_length=50)),
                ('lugar_destino', models.CharField(max_length=50)),
                ('fecha', models.DateTimeField()),
                ('a_transportar', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='servicios',
            old_name='descripcion',
            new_name='a_transportar',
        ),
        migrations.RenameField(
            model_name='servicios',
            old_name='fecha_inicio',
            new_name='fecha',
        ),
        migrations.AlterField(
            model_name='servicios',
            name='estado',
            field=models.CharField(choices=[('PH', 'Por hacer'), ('EP', 'En proceso'), ('TE', 'Terminado'), ('FI', 'Firmado')], default='PH', max_length=2),
        ),
    ]
