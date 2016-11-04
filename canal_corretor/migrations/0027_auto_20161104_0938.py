# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-04 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canal_corretor', '0026_auto_20161104_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='img',
            field=models.ImageField(blank=True, upload_to='/static/img/cat/', verbose_name='Insira uma imagem'),
        ),
        migrations.AlterField(
            model_name='empreendimento',
            name='img',
            field=models.ImageField(blank=True, upload_to='/static/img/ep/', verbose_name='Insira uma imagem:'),
        ),
        migrations.AlterField(
            model_name='material',
            name='img',
            field=models.ImageField(blank=True, upload_to='/static/img/upload/', verbose_name='Insira uma imagem'),
        ),
    ]