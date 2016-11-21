from django.contrib import admin
from .models import Libros, LibrosAdmin, Generos, Editoriales, EditorialesAdmin, Autores, AutoresAdmin, Asignacion, Asignacion2

admin.site.register(Generos)
admin.site.register(Libros, LibrosAdmin)
admin.site.register(Editoriales, EditorialesAdmin)
admin.site.register(Autores, AutoresAdmin)
admin.site.register(Asignacion)
admin.site.register(Asignacion2)
