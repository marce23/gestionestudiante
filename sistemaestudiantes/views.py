from django.shortcuts import render,render_to_response
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from django.http import HttpResponseRedirect

from sistemaestudiantes.models import Entrada

from django.forms import ModelForm
from django.core.context_processors import csrf

class FormularioEstudiante(ModelForm):
	class Meta:
		model = Entrada
		exclude = ["id"]

def main(request):
	entrada = Entrada.objects.all().order_by("-nombreEstudiante")#rescata todos los datos de la tablas y ordena por fecha
# mando los datos a la vista
	return render_to_response("listado.html",dict(entrada=entrada, user=request.user))

def add(request):
	p=dict(form=FormularioEstudiante(), user=request.user)
	p.update(csrf(request))
	return render_to_response("nuevoEstudiante.html", p)

def nuevoEstudiante(request):
	p= request.POST #le asigno a la variable p los parametros del estudiante
	estudiante= Entrada()
	estudiante= FormularioEstudiante(p,instance=estudiante)
	estudiante.save()

	return HttpResponseRedirect(reverse("sistemaestudiantes.views.main"))

def entrada(request,pk):
	##entrada.object.get --> SELECT * FROM entrada WHERE id=pk
	identrada= Entrada.objects.get(pk=int(pk))
	p=dict(entrada=identrada, form=FormularioEstudiante)
	p.update(csrf(request))
	return render_to_response("estudiante.html",p)

def eliminar(request,pk):
	estudiante=Entrada.objects.get(pk=int(pk))
	estudiante.delete()
	return HttpResponseRedirect(reverse("sistemaestudiantes.views.main"))

def update(request,pk):
	estudiante= Entrada.objects.get(pk=int(pk))
	p=dict(estudiante=estudiante, form=FormularioEstudiante(instance=estudiante))
	p.update(csrf(request))
	return render_to_response("modificarEstudiante.html",p)


def updateestudiante(request,pk):
	p= request.POST
	estmodificado = Entrada.objects.get(pk=int(pk))	
	
	estmodificado.apellidos = p['apellidos']
	estmodificado.nombreEstudiante = p['nombreEstudiante']
	estmodificado.direccion = p['direccion']
	estmodificado.telefono = p['telefono']
	estmodificado.estadocivil = p['estadocivil']
	estmodificado.genero = p['generoEstudiante']
	estmodificado.email = p['email']
	estmodificado.semestre = p['semestre']
	estmodificado.promedio = p['promedio']

	estmodificado.save()
	
	return HttpResponseRedirect(reverse("sistemaestudiantes.views.main"))


	class Formulario(ModelForm):
		class Meta:
			model = Formulario
			exclude = ["id"]