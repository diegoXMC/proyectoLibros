
from django.db import models
from django.utils import timezone
from django.contrib import admin

class Editoriales(models.Model):
    NombreE = models.CharField(max_length=200)
    Direccion = models.TextField()

    def __str__(self):
        return self.NombreE

class Generos(models.Model):
    NombreG = models.CharField(max_length=200)

    def __str__(self):
        return self.NombreG

class Libros(models.Model):
    creador = models.ForeignKey('auth.User')
    Titulo = models.CharField(max_length=200)
    Autor = models.CharField(max_length=200)
    Genero = models.ForeignKey(Generos, null=True, blank=True)
    Editorial = models.ManyToManyField(Editoriales, through='Asignacion')
    Resena = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Titulo

class Asignacion(models.Model):
    Libro = models.ForeignKey(Libros, on_delete=models.CASCADE)
    Editorial = models.ForeignKey(Editoriales, on_delete=models.CASCADE)

class AsignacionInLine(admin.TabularInline):
    model = Asignacion
    extra = 1

class EditorialesAdmin(admin.ModelAdmin):
    inlines = (AsignacionInLine,)

class LibrosAdmin (admin.ModelAdmin):
    inlines = (AsignacionInLine,)
