# Generated by Django 3.0.4 on 2020-06-10 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_transporte', '0022_catalago_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalago',
            name='stock',
        ),
    ]
