# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-10 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canal_corretor', '0002_auto_20161109_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corretor',
            name='cep',
            field=models.CharField(blank=True, max_length=16, verbose_name=' Cep*:'),
        ),
        migrations.AlterField(
            model_name='corretor',
            name='phone',
            field=models.CharField(max_length=16, verbose_name='Celular:'),
        ),
        migrations.AlterField(
            model_name='corretor',
            name='telefone',
            field=models.CharField(blank=True, max_length=16, verbose_name='Telefone:'),
        ),
        migrations.AlterField(
            model_name='imobiliaria',
            name='creci_f',
            field=models.CharField(blank=True, max_length=12, verbose_name=' Creci Físico *: '),
        ),
    ]
