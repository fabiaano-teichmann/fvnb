# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-04 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canal_corretor', '0030_auto_20161104_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empreendimento',
            name='img',
            field=models.ImageField(blank=True, upload_to='/static/img', verbose_name='Insira uma imagem:'),
        ),
    ]