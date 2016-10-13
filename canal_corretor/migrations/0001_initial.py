# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-13 20:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo:')),
                ('sub_titulo', models.CharField(max_length=150, verbose_name='Sub Titulo:')),
                ('descricao', models.TextField(verbose_name='Descrição:')),
            ],
        ),
        migrations.CreateModel(
            name='Corretor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('creci', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('cidade', models.CharField(default='none', max_length=200)),
                ('endereco', models.CharField(max_length=254)),
                ('cep', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Empreendimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Titulo:')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('img', models.ImageField(blank=True, upload_to=None, verbose_name='Insira uma imagem')),
                ('lancamento', models.DateTimeField(blank=True, null=True, verbose_name='Data prevista para lançamento')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='canal_corretor.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=200)),
                ('url', models.URLField(blank=True, verbose_name='Link para arquivos de texto')),
                ('img', models.ImageField(blank=True, upload_to='/upload/', verbose_name='Insira uma imagem')),
                ('empreendimento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='canal_corretor.Empreendimento')),
            ],
        ),
    ]
