# Generated by Django 5.0.1 on 2024-03-22 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PuntoCom', '0002_contacto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='correo_contacto',
            field=models.EmailField(max_length=100),
        ),
    ]
