# Generated by Django 3.0.4 on 2020-06-18 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_transporte', '0033_merge_20200618_1439'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agenda',
            old_name='fecha_origen',
            new_name='fecha_inicio',
        ),
        migrations.RenameField(
            model_name='servicios',
            old_name='lugar_origen',
            new_name='lugar_inicio',
        ),
    ]
