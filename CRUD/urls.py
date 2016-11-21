from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^inicio/$', views.show_libros),
    url(r'^inicio/(?P<pk>[0-9]+)/$', views.libro_detalle),
    url(r'^nuevo/$', views.libro_nuevo, name='libro_nuevo'),
    url(r'^nuevo_usuario/$', views.nuevo_usuario, name='nuevo_usuario'),
    url(r'^ingresar/$', views.ingresar, name='ingresar'),
    url(r'^cerrar/$', views.cerrar),
]
