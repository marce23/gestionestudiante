from django.shortcuts import render,render_to_response
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import HttpResponseRedirect
from sistemaestudiantes.models import Entrada, Formulario, Notas, Practica
from django.forms import ModelForm
from django.core.context_processors import csrf
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required                                          

class FormularioEstudiante(ModelForm):
	class Meta:
		model = Entrada
		exclude = ["id"]

def main(request):
	entrada = Entrada.objects.all().order_by("-nombreEstudiante")#rescata todos los datos de la tablas y ordena por fecha
# mando los datos a la vista
	return render_to_response("listado.html",dict(entrada=entrada, user=request.user))

def salir(request):
	logout(request)
	return HttpResponseRedirect(reverse("sistemaestudiantes.views.main"))	

@login_required(login_url='/')
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
	identrada= Entrada.objects.get(pk=int(pk))
	misnotas=Notas.objects.filter(identrad=identrada)
	mispracticas=Practica.objects.filter(identrada=identrada)
	p=dict(entrada=identrada, form=FormularioEstudiante, misnotas=misnotas, mispracticas=mispracticas)
	p.update(csrf(request))
	return render_to_response("estudiante.html",p)

@login_required(login_url='/')
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

class Form(ModelForm):
    class Meta:
        model = Formulario
        exclude = ["id"]

def regform(request, pk):
    p = request.POST
    form = Formulario(idform=Entrada.objects.get(pk=pk))
    fr = Form(p, instance=form)
    fr.save()
    return HttpResponseRedirect(reverse("sistemaestudiantes.views.main"))

def addform(request, pk):
	identrada = Entrada.objects.get(pk=int(pk))
	p=dict(entrada=identrada, form=Form())
	p.update(csrf(request))
	return render_to_response("formulario.html", p)

class FormNotas(ModelForm):
    class Meta:
        model = Notas
        exclude = ["id"]

def regnota(request, pk):
    p = request.POST
    notas= Notas(identrad=Entrada.objects.get(pk=pk))
    fn = FormNotas(p, instance=notas)
    fn.save()
    return HttpResponseRedirect(reverse("sistemaestudiantes.views.main"))

def addnota(request, pk):
	identrada = Entrada.objects.get(pk=int(pk))
	p=dict(entrada=identrada, form=FormNotas())
	p.update(csrf(request))
	return render_to_response("notas.html", p)


class FormPractica(ModelForm):
    class Meta:
        model = Practica
        exclude = ["id"]

def regpractica(request, pk):
    p = request.POST
    practica = Practica(identrada=Entrada.objects.get(pk=pk))
    fp = FormPractica(p, instance=practica)
    fp.save()
    return HttpResponseRedirect(reverse("sistemaestudiantes.views.main"))

def addpractica(request, pk):
	identrada = Entrada.objects.get(pk=int(pk))
	p=dict(entrada=identrada, form=FormPractica())
	p.update(csrf(request))
	return render_to_response("practica.html", p)