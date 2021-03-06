# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-13 13:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('canal_corretor', '0007_auto_20170112_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='ep_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='image', to='canal_corretor.Empreendimento'),
        ),
        migrations.AlterField(
            model_name='material',
            name='ep_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='material', to='canal_corretor.Empreendimento'),
        ),
        migrations.AlterField(
            model_name='tabela',
            name='ep_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tabela', to='canal_corretor.Empreendimento'),
        ),
    ]
