# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Editoriales',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('NombreE', models.CharField(max_length=200)),
                ('Direccion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Generos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('NombreG', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=200)),
                ('Autor', models.CharField(max_length=200)),
                ('Resena', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Editorial', models.ManyToManyField(to='CRUD.Editoriales', through='CRUD.Asignacion')),
                ('Genero', models.ForeignKey(to='CRUD.Generos', blank=True, null=True)),
                ('creador', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='asignacion',
            name='Editorial',
            field=models.ForeignKey(to='CRUD.Editoriales'),
        ),
        migrations.AddField(
            model_name='asignacion',
            name='Libro',
            field=models.ForeignKey(to='CRUD.Libros'),
        ),
    ]
