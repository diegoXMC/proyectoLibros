from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^inicio/$', views.show_libros),
    url(r'^inicio/(?P<pk>[0-9]+)/$', views.libro_detalle),
    url(r'^nuevo/$', views.libro_nuevo, name='libro_nuevo'),
    url(r'^nuevo_usuario/$', views.nuevo_usuario, name='nuevo_usuario'),
    url(r'^ingresar/$', views.ingresar, name='ingresar'),
    url(r'^cerrar/$', views.cerrar),
    url(r'^editar/(?P<pk>[0-9]+)/$', views.libro_editar, name='libro_editar'),
    url(r'^borrar/(?P<pk>[0-9]+)/$', views.libro_borrar, name='libro_borrar'),
    url(r'^nuevo_autor/$', views.autores_nuevo, name='autores_nuevo'),
    url(r'^editar_autor/(?P<pk>[0-9]+)/$', views.autores_editar, name='autores_editar'),
    url(r'^mostrar_autor/$', views.show_autores),
    url(r'^borrar_autor/(?P<pk>[0-9]+)/$', views.autores_borrar, name='autores_borrar'),
    url(r'^nuevo_genero$', views.generos_nuevo, name='generos_nuevo'),
    url(r'^editar_genero/(?P<pk>[0-9]+)/$', views.generos_editar, name='generos_editar'),
    url(r'^mostrar_genero/$', views.show_generos),
    url(r'^borrar_genero/(?P<pk>[0-9]+)/$', views.generos_borrar, name='generos_borrar'),
]
