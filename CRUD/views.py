from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Libros

def show_libros(request):
    libro = Libros.objects.all()
    return render(request, 'libros_list.html', {'libro': libro})

def libro_detalle(request, pk):
    libro = get_object_or_404(Libros, pk=pk)
    return render(request, 'libros_detalle.html', {'libro': libro})
