# Generated by Django 4.2.11 on 2024-03-27 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PuntoCom', '0005_servicios_imagen_trabajo_alter_servicios_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='estado_correo',
            field=models.BooleanField(default=False),
        ),
    ]