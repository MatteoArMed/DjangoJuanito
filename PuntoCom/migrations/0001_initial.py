# Generated by Django 5.0.1 on 2024-01-25 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_descripcion', models.CharField(max_length=200)),
                ('fecha_publicacion', models.DateTimeField(verbose_name='Fecha Publicación')),
            ],
        ),
        migrations.CreateModel(
            name='Trabajos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lugar_trabajo', models.CharField(max_length=200)),
                ('descripcion_trabajo', models.CharField(max_length=1000)),
                ('tipo_trabajo', models.CharField(max_length=200)),
            ],
        ),
    ]
