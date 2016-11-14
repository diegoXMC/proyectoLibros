# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignacion2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Autores',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('NombreA', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='libros',
            name='Autor',
        ),
        migrations.AddField(
            model_name='asignacion2',
            name='Autor',
            field=models.ForeignKey(to='CRUD.Autores'),
        ),
        migrations.AddField(
            model_name='asignacion2',
            name='Libro',
            field=models.ForeignKey(to='CRUD.Libros'),
        ),
        migrations.AddField(
            model_name='libros',
            name='Autor',
            field=models.ManyToManyField(through='CRUD.Asignacion2', to='CRUD.Autores'),
        ),
    ]
