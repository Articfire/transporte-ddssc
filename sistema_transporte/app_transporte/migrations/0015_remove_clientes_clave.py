# Generated by Django 3.0.4 on 2020-05-28 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_transporte', '0014_auto_20200521_1931'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientes',
            name='clave',
        ),
    ]
