# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-01 18:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canal_corretor', '0018_auto_20161101_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='img',
            field=models.ImageField(blank=True, upload_to='media/img', verbose_name='Insira uma imagem'),
        ),
    ]