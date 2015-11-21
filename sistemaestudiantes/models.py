from django.db import models

# Create your models here. 	
class Entrada(models.Model):

	apellidos = models.CharField(max_length=100)
	nombreEstudiante	= models.CharField(max_length=100)
	identificacion = models.CharField(max_length=100)
	tipoIden= (
		('Cedula', 'Cedula'),
		('Tarjeta de Identidad', 'Tarjeta de Identidad'),
	)	
	tipoidentidad= models.CharField(max_length=20, choices= tipoIden)
	direccion = models.CharField(max_length=100)
	telefono = models.CharField(max_length=50)
	estado = (
		('Soltero', 'Soltero'),
		('Casado', 'Casado'),
		('Separado', 'Separado'),
		('Viudo', 'Viudo'),
		
	)	
	estadocivil= models.CharField(max_length=9, choices= estado)
	genero = (
		('Masculino', 'Masculino'),
		('Femenino', 'Femenino'),
	)	
	generoEstudiante= models.CharField(max_length=9, choices= genero)
	email  = models.CharField(max_length=100)
	semestre  = models.IntegerField(default=0)
	promedio  = models.FloatField()
	

	def __str__(self):
		return self.nombreEstudiante

class Formulario(models.Model):

	modalidad = (
		('P', 'Pregrado'),
		('O', 'Postgrado'),
		('D', 'Eduacion a distancia'),
	)	
	modalidadEstudio= models.CharField(max_length=1, choices= modalidad)
	nombreEstudiante	= models.CharField(max_length=100)
	identificacion = models.CharField(max_length=100)
	tipoIden= (
		('Cedula', 'Cedula'),
		('Tarjeta de Identidad', 'Tarjeta de Identidad'),
	)	
	tipoidentidad= models.CharField(max_length=20, choices= tipoIden)
	direccion = models.CharField(max_length=100)
	telefono = models.CharField(max_length=50)
	estado = (
		('Soltero', 'Soltero'),
		('Casado', 'Casado'),
		('Separado', 'Separado'),
		('Viudo', 'Viudo'),
		
	)	
	estadocivil= models.CharField(max_length=9, choices= estado)
	genero = (
		('Masculino', 'Masculino'),
		('Femenino', 'Femenino'),
	)	
	generoEstudiante= models.CharField(max_length=9, choices= genero)
	email  = models.CharField(max_length=100)
	programa = (
		('E', 'Enfermeria Superior'),
		('T', 'Trabajo Social'),
		('P', 'Psicologia'),
		('N', 'Nutricion y Dietetica'),
		('O', 'Terapia Ocupacional'),
		('C', 'Contaduria publica'),
		('M', 'Administracion de Empresas'),
		('D', 'Derecho'),
		('I', 'Ingenieria de Sistemas'),
		('A', 'Ingenieria Ambiental'),
		('P', 'Ingenieria Mecatronica'),
	)	
	programa= models.CharField(max_length=1, choices= programa)
	colegio= models.CharField(max_length=200)
	puntaje= models.FloatField()


