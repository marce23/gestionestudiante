# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('apellidos', models.CharField(max_length=100)),
                ('nombreEstudiante', models.CharField(max_length=100)),
                ('identificacion', models.CharField(max_length=100)),
                ('tipoidentidad', models.CharField(max_length=20, choices=[(b'Cedula', b'Cedula'), (b'Tarjeta de Identidad', b'Tarjeta de Identidad')])),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=50)),
                ('estadocivil', models.CharField(max_length=9, choices=[(b'Soltero', b'Soltero'), (b'Casado', b'Casado'), (b'Separado', b'Separado'), (b'Viudo', b'Viudo')])),
                ('generoEstudiante', models.CharField(max_length=9, choices=[(b'Masculino', b'Masculino'), (b'Femenino', b'Femenino')])),
                ('email', models.CharField(max_length=100)),
                ('semestre', models.IntegerField(default=0)),
                ('promedio', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('modalidadEstudio', models.CharField(max_length=1, choices=[(b'P', b'Pregrado'), (b'O', b'Postgrado'), (b'D', b'Eduacion a distancia')])),
                ('nombreEstudiante', models.CharField(max_length=100)),
                ('identificacion', models.CharField(max_length=100)),
                ('tipoidentidad', models.CharField(max_length=20, choices=[(b'Cedula', b'Cedula'), (b'Tarjeta de Identidad', b'Tarjeta de Identidad')])),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=50)),
                ('estadocivil', models.CharField(max_length=9, choices=[(b'Soltero', b'Soltero'), (b'Casado', b'Casado'), (b'Separado', b'Separado'), (b'Viudo', b'Viudo')])),
                ('generoEstudiante', models.CharField(max_length=9, choices=[(b'Masculino', b'Masculino'), (b'Femenino', b'Femenino')])),
                ('email', models.CharField(max_length=100)),
                ('programa', models.CharField(max_length=1, choices=[(b'E', b'Enfermeria Superior'), (b'T', b'Trabajo Social'), (b'P', b'Psicologia'), (b'N', b'Nutricion y Dietetica'), (b'O', b'Terapia Ocupacional'), (b'C', b'Contaduria publica'), (b'M', b'Administracion de Empresas'), (b'D', b'Derecho'), (b'I', b'Ingenieria de Sistemas'), (b'A', b'Ingenieria Ambiental'), (b'P', b'Ingenieria Mecatronica')])),
                ('colegio', models.CharField(max_length=200)),
                ('puntaje', models.FloatField()),
            ],
        ),
    ]
