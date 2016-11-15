from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^inicio/$', views.show_libros),
    url(r'^inicio/(?P<pk>[0-9]+)/$', views.libro_detalle),
]
