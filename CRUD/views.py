from django.contrib import messages, admin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.utils import timezone
from .models import Libros, Autores, Asignacion2, Asignacion
from .forms import LibroForm
from django.template.context import RequestContext
from django.http.response import HttpResponseRedirect

def nuevo_usuario(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/libros/inicio')
    if request.method=='POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/libros/ingresar')
    else:
        formulario = UserCreationForm()
    return render_to_response('nuevo_usuario.html', {'formulario':formulario}, context_instance=RequestContext(request))

def ingresar(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/libros/inicio')
    if request.method=='POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/libros/inicio')
                else:
                    return render_to_response('no_activo.html', context_instance=RequestContext(request))
            else:
                messages.add_message(request, messages.SUCCESS, 'El Usuario no existe')
                return HttpResponseRedirect('/libros/inicio')
    else:
        formulario = AuthenticationForm()
    return render_to_response('ingresar.html', {'formulario':formulario}, context_instance=RequestContext(request))

def show_libros(request):
    libro = Libros.objects.all()
    usuario = request.user.is_anonymous()
    return render(request, 'libros_list.html', {'libro': libro, 'ususario':usuario})

def libro_detalle(request, pk):
    libro = get_object_or_404(Libros, pk=pk)
    autor = Asignacion2.objects.filter(Libro = pk)
    usuario = request.user.is_anonymous()
    return render(request, 'libros_detalle.html', {'libro': libro, 'autor':autor, 'usuario':usuario})

@login_required(login_url='/libros/ingresar')
def libro_nuevo(request):
    usuario = request.user.is_anonymous()
    if request.method == "POST":
        formulario = LibroForm(request.POST)
        if formulario.is_valid():
            cre = request.user.id
            libro = Libros.objects.create(creador_id=cre, Titulo=formulario.cleaned_data['Titulo'], Genero=formulario.cleaned_data['Genero'], Resena=formulario.cleaned_data['Resena'])
            for autor_id in request.POST.getlist('Autor'):
                asg1 = Asignacion2(Libro_id=libro.id, Autor_id=autor_id)
                asg1.save()
            for editorial_id in request.POST.getlist('Editorial'):
                asg2 = Asignacion(Libro_id=libro.id, Editorial_id=editorial_id)
                asg2.save()
            return redirect('CRUD.views.show_libros')
    else:
        formulario = LibroForm()
    return render(request, 'libros_nuevo.html', {'formulario': formulario, 'usuario':usuario})

@login_required(login_url='/libros/ingresar')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/libros/inicio')
