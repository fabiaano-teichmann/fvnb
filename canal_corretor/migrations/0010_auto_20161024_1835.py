# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-24 20:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('canal_corretor', '0009_auto_20161024_1533'),
    ]

    operations = [
        migrations.CreateModel(
            name='CorretorAfiliado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome: * ')),
                ('nasc', models.DateField(verbose_name='Data de nascimento')),
                ('cpf', models.CharField(max_length=16, verbose_name='CPF: * ')),
                ('creci', models.CharField(max_length=12, verbose_name=' Creci Físico: * ')),
                ('telefone', models.CharField(max_length=16, verbose_name='Telefone:*')),
                ('phone', models.CharField(blank=True, max_length=16, verbose_name='Celular: * ')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail *: ')),
            ],
        ),
        migrations.DeleteModel(
            name='Autonomo',
        ),
        migrations.RemoveField(
            model_name='corretor',
            name='vinculado',
        ),
        migrations.AddField(
            model_name='corretor',
            name='bairro',
            field=models.CharField(default=False, max_length=100, verbose_name='Bairro*:'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='corretor',
            name='cep',
            field=models.CharField(default=True, max_length=16, verbose_name=' Cep*:'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='corretor',
            name='cidade',
            field=models.CharField(default=False, max_length=200, verbose_name='Cidade*:'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='corretor',
            name='endereco',
            field=models.CharField(default=False, max_length=254, verbose_name='Endereço *:'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='corretor',
            name='estado',
            field=models.CharField(choices=[('Acre', 'AC'), ('Alagoas', 'AL'), ('Amapá', 'AP'), ('Amazonas', 'AM'), ('Bahia', 'BA'), ('Ceará', 'CE'), ('Distrito Federal', 'DF'), ('Espírito Santo', 'ES'), ('Goiás', 'GO'), ('Maranhão', 'MA'), ('Mato Grosso', 'MT'), ('Mato Grosso do Sul', 'MS'), ('Minas Gerais', 'MG'), ('Pará', 'PA'), ('Paraíba', 'PB'), ('Paraná', 'PR'), ('Pernambuco', 'PE'), ('Piauí', 'PI'), ('Rio de Janeiro', 'RJ'), ('Rio Grande do Norte', 'RN'), ('Rio Grande do Sul', 'RS'), ('Rondônia', 'RO'), ('Roraima', 'RR'), ('Santa Catarina', 'SC'), ('São Paulo', 'SP'), ('Sergipe', 'SE'), ('Tocantins', 'TO')], default=False, max_length=100, verbose_name='Estado*:'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='corretor',
            name='site',
            field=models.URLField(blank=True, verbose_name='site'),
        ),
        migrations.AddField(
            model_name='imobiliaria',
            name='ativacao',
            field=models.CharField(blank=True, choices=[('1', 'Inativo'), ('2', 'Ativo')], default='Inativo', max_length=10),
        ),
        migrations.AlterField(
            model_name='corretor',
            name='cpf',
            field=models.CharField(max_length=16, verbose_name='Cpf:'),
        ),
        migrations.AlterField(
            model_name='corretor',
            name='creci',
            field=models.CharField(max_length=12, verbose_name='Creci Físico*:'),
        ),
        migrations.AlterField(
            model_name='corretor',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-mail*:'),
        ),
        migrations.AlterField(
            model_name='corretor',
            name='nasc',
            field=models.DateField(verbose_name='Data de nascimento*:'),
        ),
        migrations.AlterField(
            model_name='corretor',
            name='nome',
            field=models.CharField(max_length=150, verbose_name='Nome*:'),
        ),
        migrations.AlterField(
            model_name='corretor',
            name='phone',
            field=models.CharField(blank=True, max_length=16, verbose_name='Celular:'),
        ),
        migrations.AlterField(
            model_name='corretor',
            name='telefone',
            field=models.CharField(max_length=16, verbose_name='Telefone:'),
        ),
        migrations.AddField(
            model_name='corretorafiliado',
            name='vinculado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canal_corretor.Imobiliaria', verbose_name='Imobiliária vinculada'),
        ),
    ]
