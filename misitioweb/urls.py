"""misitioweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^entrada/(?P<pk>\d+)/$','sistemaestudiantes.views.entrada'),
    url(r'^add/$','sistemaestudiantes.views.add'), #esta es para enlazar el index con la pagina nuevoEstudiante.html
    url(r'^eliminar/(?P<pk>\d+)/$','sistemaestudiantes.views.eliminar'), 
    url(r'^update/(?P<pk>\d+)/$','sistemaestudiantes.views.update'), 
    url(r'^updateestudiante/(?P<pk>\d+)/$','sistemaestudiantes.views.updateestudiante'), 
    url(r'^nuevoEstudiante/$','sistemaestudiantes.views.nuevoEstudiante'), #esta url es la encargada de rescatar los parametros y hacer el insert en los parametros
    #url(r'^month/(\d+)/(\d+)/$','blog.views.month'),
    #url(r'^poncomentario/(\d+)/$','blog.views.poncomentario'),

    url(r'', 'sistemaestudiantes.views.main'),
]
