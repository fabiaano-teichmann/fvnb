# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-13 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canal_corretor', '0009_auto_20170113_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='iframe',
            field=models.URLField(max_length=250, verbose_name='Insira iframe'),
        ),
    ]
