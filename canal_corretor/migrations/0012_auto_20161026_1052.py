# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-26 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canal_corretor', '0011_auto_20161026_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imobiliaria',
            name='ativacao',
            field=models.CharField(blank=True, choices=[('1', 'Inativo'), ('2', 'Ativo')], default=1, max_length=10),
        ),
    ]