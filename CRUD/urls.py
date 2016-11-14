from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.show_libros),
    url(r'^inicio/$', views.show_libros),
]
