# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-13 16:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canal', '0007_empreendimento_lancamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empreendimento',
            name='img',
            field=models.ImageField(blank=True, height_field=374, upload_to=None, width_field=1024),
        ),
    ]
