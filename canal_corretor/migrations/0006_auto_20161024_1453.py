# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-24 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canal_corretor', '0005_auto_20161024_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autonomo',
            name='status',
            field=models.CharField(blank=True, choices=[('1', 'Inativo'), ('2', 'Ativo')], max_length=10),
        ),
    ]
