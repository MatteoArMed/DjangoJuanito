# Generated by Django 5.0.1 on 2024-03-22 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PuntoCom', '0003_alter_contacto_correo_contacto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_trabajo', models.CharField(max_length=255)),
                ('sub_titulo', models.CharField(max_length=255)),
                ('descripcion', models.TextField(max_length=1000)),
                ('precio', models.IntegerField(max_length=11)),
            ],
        ),
        migrations.AlterField(
            model_name='contacto',
            name='fecha_contacto',
            field=models.DateField(auto_now_add=True),
        ),
    ]
