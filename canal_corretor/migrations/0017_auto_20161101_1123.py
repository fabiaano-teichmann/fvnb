# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-01 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canal_corretor', '0016_auto_20161101_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empreendimento',
            name='img',
            field=models.ImageField(blank=True, upload_to='static/img', verbose_name='Insira uma imagem:'),
        ),
        migrations.AlterField(
            model_name='material',
            name='file',
            field=models.FileField(blank=True, upload_to='static/doc', verbose_name='Arquivos texto'),
        ),
    ]
