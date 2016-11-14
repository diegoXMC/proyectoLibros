from django.shortcuts import render
from django.utils import timezone
from .models import Libros

def show_libros(request):
    libro = Libros.objects.all()
    return render(request, 'libros_list.html', {'libro': libro})
