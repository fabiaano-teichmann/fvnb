# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-04 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canal_corretor', '0035_auto_20161104_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='empreendimento',
            name='sub_titulo',
            field=models.CharField(default=False, max_length=150, verbose_name='Sub titulo'),
            preserve_default=False,
        ),
    ]
