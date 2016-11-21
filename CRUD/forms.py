from django import forms
from .models import Libros, Autores, Generos

class LibroForm(forms.ModelForm):

  class Meta:
    model = Libros
    fields = ('Titulo', 'Genero', 'Autor', 'Editorial', 'Resena',)

def __init__ (self, *args, **kwargs):
    super(LibroForm, self).__init__(*args, **kwargs)

    self.fields["Autor"].widget = forms.widgets.CheckboxSelectMultiple()
    self.fields["Autor"].help_text = "Autores del Libro"
    self.fields["Autor"].queryset = Autores.objects.all()

    self.fields["Editorial"].widget = forms.widgets.CheckboxSelectMultiple()
    self.fields["Editorial"].help_text = "Editoriales del Libro"
    self.fields["Editorial"].queryset = Editoriales.objects.all()

class AutorForm(forms.ModelForm):

  class Meta:
    model = Autores
    fields = ('NombreA',)

class GeneroForm(forms.ModelForm):

  class Meta:
    model = Generos
    fields = ('NombreG',)
