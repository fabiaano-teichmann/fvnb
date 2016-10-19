# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-19 17:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Nome:')),
                ('sub_titulo', models.CharField(max_length=150, verbose_name='Sub Titulo:')),
            ],
        ),
        migrations.CreateModel(
            name='Corretor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome: (campo obrigatório)')),
                ('nasc', models.DateField(verbose_name='Data de nascimento')),
                ('cpf', models.CharField(max_length=16, verbose_name='Cep: (Campo obrigatório)')),
                ('creci', models.CharField(max_length=12, verbose_name=' Creci Físico: (campo obrigatório)')),
                ('telefone', models.CharField(max_length=16, verbose_name='Telefone:')),
                ('phone', models.CharField(blank=True, max_length=16, verbose_name='Celular: ')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail: (campo obrigatório)')),
                ('site', models.URLField(blank=True, verbose_name='site')),
                ('endereco', models.CharField(max_length=254, verbose_name='Endereço:(campo obrigatório)')),
                ('bairro', models.CharField(max_length=100, verbose_name='Bairro: (campo obrigatório)')),
                ('cidade', models.CharField(max_length=200, verbose_name='Cidade: (campo obrigatório)')),
                ('cep', models.CharField(max_length=16, verbose_name=' Cep: (campo obrigatório)')),
                ('estado', models.CharField(choices=[('Acre', 'AC'), ('Alagoas', 'AL'), ('Amapá', 'AP'), ('Amazonas', 'AM'), ('Bahia', 'BA'), ('Ceará', 'CE'), ('Distrito Federal', 'DF'), ('Espírito Santo', 'ES'), ('Goiás', 'GO'), ('Maranhão', 'MA'), ('Mato Grosso', 'MT'), ('Mato Grosso do Sul', 'MS'), ('Minas Gerais', 'MG'), ('Pará', 'PA'), ('Paraíba', 'PB'), ('Paraná', 'PR'), ('Pernambuco', 'PE'), ('Piauí', 'PI'), ('Rio de Janeiro', 'RJ'), ('Rio Grande do Norte', 'RN'), ('Rio Grande do Sul', 'RS'), ('Rondônia', 'RO'), ('Roraima', 'RR'), ('Santa Catarina', 'SC'), ('São Paulo', 'SP'), ('Sergipe', 'SE'), ('Tocantins', 'TO')], max_length=100, verbose_name='Estado: (campo obrigatório)')),
            ],
        ),
        migrations.CreateModel(
            name='Empreendimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Nome:(campo obrigatório)')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('img', models.ImageField(blank=True, upload_to=None, verbose_name='Insira uma imagem:')),
                ('lancamento', models.DateField(blank=True, null=True, verbose_name='Data prevista para lançamento')),
                ('estado', models.CharField(blank=True, choices=[('Acre', 'AC'), ('Alagoas', 'AL'), ('Amapá', 'AP'), ('Amazonas', 'AM'), ('Bahia', 'BA'), ('Ceará', 'CE'), ('Distrito Federal', 'DF'), ('Espírito Santo', 'ES'), ('Goiás', 'GO'), ('Maranhão', 'MA'), ('Mato Grosso', 'MT'), ('Mato Grosso do Sul', 'MS'), ('Minas Gerais', 'MG'), ('Pará', 'PA'), ('Paraíba', 'PB'), ('Paraná', 'PR'), ('Pernambuco', 'PE'), ('Piauí', 'PI'), ('Rio de Janeiro', 'RJ'), ('Rio Grande do Norte', 'RN'), ('Rio Grande do Sul', 'RS'), ('Rondônia', 'RO'), ('Roraima', 'RR'), ('Santa Catarina', 'SC'), ('São Paulo', 'SP'), ('Sergipe', 'SE'), ('Tocantins', 'TO')], max_length=100, verbose_name='Estado: (campo obrigatório)')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='canal_corretor.Categoria', verbose_name='categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Imobiliaria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, upload_to=None, verbose_name='Insira uma imagem:')),
                ('razao', models.CharField(max_length=200, verbose_name=' Razão social:(campo obrigatório)')),
                ('creci_j', models.CharField(max_length=6, verbose_name='Creci Jurídico(campo obrigatório)')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome Fantasia:(campo obrigatório)')),
                ('cnpj', models.CharField(max_length=14, verbose_name=' Cnpj:(campo obrigatório)')),
                ('endereco', models.CharField(max_length=254, verbose_name='Endereço:(campo obrigatório)')),
                ('bairro', models.CharField(blank=True, max_length=100, verbose_name='Bairro: (campo obrigatório)')),
                ('cidade', models.CharField(max_length=200, verbose_name='Cidade: (campo obrigatório)')),
                ('cep', models.CharField(max_length=12, verbose_name=' Cep: (campo obrigatório)')),
                ('estado', models.CharField(choices=[('Acre', 'AC'), ('Alagoas', 'AL'), ('Amapá', 'AP'), ('Amazonas', 'AM'), ('Bahia', 'BA'), ('Ceará', 'CE'), ('Distrito Federal', 'DF'), ('Espírito Santo', 'ES'), ('Goiás', 'GO'), ('Maranhão', 'MA'), ('Mato Grosso', 'MT'), ('Mato Grosso do Sul', 'MS'), ('Minas Gerais', 'MG'), ('Pará', 'PA'), ('Paraíba', 'PB'), ('Paraná', 'PR'), ('Pernambuco', 'PE'), ('Piauí', 'PI'), ('Rio de Janeiro', 'RJ'), ('Rio Grande do Norte', 'RN'), ('Rio Grande do Sul', 'RS'), ('Rondônia', 'RO'), ('Roraima', 'RR'), ('Santa Catarina', 'SC'), ('São Paulo', 'SP'), ('Sergipe', 'SE'), ('Tocantins', 'TO')], max_length=100, verbose_name='Estado: (campo obrigatório)')),
                ('telefone', models.CharField(blank=True, max_length=16, verbose_name='Telefone:')),
                ('phone', models.CharField(blank=True, max_length=16, verbose_name='Celular: ')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail: (campo obrigatório)')),
                ('site', models.URLField(blank=True, verbose_name='site')),
                ('resp', models.CharField(max_length=150, verbose_name='(Corretor Resposável:campo obrigatório)')),
                ('email_resp', models.CharField(max_length=200, verbose_name='Email do Responsável:')),
                ('cpf', models.CharField(max_length=18, verbose_name='Cep: (Campo obrigatório)')),
                ('creci_f', models.CharField(max_length=12, verbose_name=' Creci Físico: (campo obrigatório)')),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome: (campo obrigatório)')),
                ('descricao', models.CharField(blank=True, max_length=200)),
                ('file', models.FileField(blank=True, upload_to=None, verbose_name='Arquivos texto')),
                ('img', models.ImageField(blank=True, upload_to=None, verbose_name='Insira uma imagem')),
                ('empreendimento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='canal_corretor.Empreendimento')),
            ],
        ),
        migrations.AddField(
            model_name='corretor',
            name='vinculado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canal_corretor.Imobiliaria', verbose_name='Imobiliária vinculada'),
        ),
    ]
