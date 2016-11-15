from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.show_libros),
    url(r'^inicio/$', views.show_libros),
    url(r'^detalle/(?P<pk>[0-9]+)/$', views.detale_libro),
]
