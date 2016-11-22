from django.contrib import messages, admin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.utils import timezone
from .models import Libros, Autores, Asignacion2, Asignacion, Generos
from .forms import LibroForm, AutorForm, GeneroForm
from django.template.context import RequestContext
from django.http.response import HttpResponseRedirect

def nuevo_usuario(request):
    usuario = request.user
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/libros/inicio')
    if request.method=='POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/libros/ingresar')
    else:
        formulario = UserCreationForm()
    return render_to_response('nuevo_usuario.html', {'formulario':formulario, 'usuario':usuario}, context_instance=RequestContext(request))

def ingresar(request):
    usuario = request.user
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
    return render_to_response('ingresar.html', {'formulario':formulario, 'usuario':usuario}, context_instance=RequestContext(request))

@login_required(login_url='/libros/ingresar')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/libros/inicio')

#todo lo referente a libros
def show_libros(request):
    libro = Libros.objects.all()
    usuario = request.user
    return render(request, 'libros_list.html', {'libro': libro, 'usuario':usuario})

def libro_detalle(request, pk):
    libro = get_object_or_404(Libros, pk=pk)
    autor = Asignacion2.objects.filter(Libro = pk)
    usuario = request.user
    return render(request, 'libros_detalle.html', {'libro': libro, 'autor':autor, 'usuario':usuario})

@login_required(login_url='/libros/ingresar')
def libro_editar(request, pk):
    usuario = request.user
    libro = get_object_or_404(Libros, pk=pk)
    if request.method == "POST":
        formulario = LibroForm(request.POST, instance=libro)
        if formulario.is_valid():
            libro = formulario.save(commit=False)
            libro.author = request.user
            libro.save()
            return redirect('CRUD.views.libro_detalle', pk=libro.pk)
    else:
        formulario = LibroForm(instance=libro)
    return render(request, 'nuevo_libro.html', {'formulario': formulario, 'usuario':usuario})

@login_required(login_url='/libros/ingresar')
def libro_borrar(request, pk):
    libro = get_object_or_404(Libros, pk=pk)
    libro.delete()
    return render(request, 'libros_list.html', {'libro': libro, 'usuario':usuario})

@login_required(login_url='/libros/ingresar')
def libro_nuevo(request):
    usuario = request.user
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
    return render(request, 'nuevo_libro.html', {'formulario': formulario, 'usuario':usuario})

#todo lo referente a autores
def show_autores(request):
    autor = Autores.objects.all()
    usuario = request.user
    return render(request, 'autores_list.html', {'autor': autor, 'usuario':usuario})

@login_required(login_url='/libros/ingresar')
def autores_editar(request, pk):
    usuario = request.user
    autor = get_object_or_404(Autores, pk=pk)
    if request.method == "POST":
        formulario = AutorForm(request.POST, instance=autor)
        if formulario.is_valid():
            autor = formulario.save(commit=False)
            autor.save()
            return redirect('CRUD.views.show_libros')
    else:
        formulario = AutorForm(instance=autor)
    return render(request, 'nuevo_autor.html', {'formulario': formulario, 'usuario':usuario})

@login_required(login_url='/libros/ingresar')
def autores_borrar(request, pk):
    usuario = request.user
    autor = get_object_or_404(Autores, pk=pk)
    autor.delete()
    return render(request, 'autores_list.html', {'autor': autor, 'usuario':usuario})

@login_required(login_url='/libros/ingresar')
def autores_nuevo(request):
    usuario = request.user
    if request.method == "POST":
        formulario = AutorForm(request.POST)
        if formulario.is_valid():
            cre = request.user.id
            autor = formulario.save(commit=False)
            autor.save()
            return redirect('CRUD.views.show_autores')
    else:
        formulario = AutorForm()
    return render(request, 'nuevo_autor.html', {'formulario': formulario, 'usuario':usuario})

#todo lo referente con los generos
def show_generos(request):
    genero = Generos.objects.all()
    usuario = request.user
    return render(request, 'generos_list.html', {'genero': genero, 'ususario':usuario})

@login_required(login_url='/libros/ingresar')
def generos_editar(request, pk):
    usuario = request.user
    genero = get_object_or_404(Generos, pk=pk)
    if request.method == "POST":
        formulario = GeneroForm(request.POST, instance=genero)
        if formulario.is_valid():
            genero = formulario.save(commit=False)
            genero.save()
            return redirect('CRUD.views.show_generos')
    else:
        formulario = GeneroForm(instance=genero)
    return render(request, 'nuevo_genero.html', {'formulario': formulario, 'usuario':usuario})

@login_required(login_url='/libros/ingresar')
def generos_borrar(request, pk):
    genero = get_object_or_404(Generos, pk=pk)
    genero.delete()
    return render(request, 'generos_list.html', {'genero': genero, 'ususario':usuario})

@login_required(login_url='/libros/ingresar')
def generos_nuevo(request):
    usuario = request.user
    if request.method == "POST":
        formulario = GeneroForm(request.POST)
        if formulario.is_valid():
            genero = formulario.save(commit=False)
            genero.save()
            return redirect('CRUD.views.show_generos')
    else:
        formulario = GeneroForm()
    return render(request, 'nuevo_genero.html', {'formulario': formulario, 'usuario':usuario})
