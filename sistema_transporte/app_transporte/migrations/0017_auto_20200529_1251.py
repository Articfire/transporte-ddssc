# Generated by Django 3.0.4 on 2020-05-29 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_transporte', '0016_auto_20200529_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicios',
            name='lugar_destino',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='servicios',
            name='lugar_inicio',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='servicios',
            name='mascota',
            field=models.CharField(max_length=20),
        ),
    ]
