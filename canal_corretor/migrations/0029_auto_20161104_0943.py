# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-04 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canal_corretor', '0028_auto_20161104_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empreendimento',
            name='img',
            field=models.ImageField(blank=True, upload_to='/static/cat/', verbose_name='Insira uma imagem:'),
        ),
    ]