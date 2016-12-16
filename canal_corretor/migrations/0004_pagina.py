# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-14 18:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canal_corretor', '0003_auto_20161214_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('sub_titulo', models.CharField(max_length=150, verbose_name='Subtitulo')),
                ('nomeimg', models.CharField(max_length=100, verbose_name='Descrição da imagem')),
                ('img', models.ImageField(upload_to='static/img/', verbose_name='Banner')),
                ('descricacao', models.TextField(verbose_name='Descrição')),
            ],
        ),
    ]