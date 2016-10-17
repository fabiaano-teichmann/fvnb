from django.db import models
from django.utils import timezone
import datetime
estado = (
	('Acre', 'AC'),
	('Alagoas','AL'),
	('Amapá','AP'),
	('Amazonas','AM'),
	('Bahia','BA'),
	('Ceará','CE'),
	('Distrito Federal', 'DF'),
	('Espírito Santo', 'ES'),
	('Goiás', 'GO'),
	('Maranhão', 'MA'),
	('Mato Grosso', 'MT'),
	('Mato Grosso do Sul', 'MS'),
	('Minas Gerais', 'MG'),
	('Pará', 'PA'),
	('Paraíba', 'PB'),
	('Paraná' ,'PR'),
	('Pernambuco', 'PE'),
	('Piauí', 'PI'),
	('Rio de Janeiro', 'RJ'),
	('Rio Grande do Norte', 'RN'),
	('Rio Grande do Sul', 'RS'),
	('Rondônia','RO'),
	('Roraima',	'RR'),
	('Santa Catarina', 'SC'),
	('São Paulo', 'SP'),
	('Sergipe',	'SE'),
	('Tocantins','TO'),
	)
tipo = (
	('J', 'Jurídica'),
	('F', 'Fisica')
	)

class Corretor(models.Model):
	nome = models.CharField(verbose_name='Nome: (campo obrigatório)',max_length=150)
	#precisa o usuário ter acesso admin
	author = models.ForeignKey ('auth.User')
	creci =  models.IntegerField(verbose_name='Registro CRECI: (campo obrigatório)', blank=False)
	tipo = models.CharField(max_length=10,verbose_name='Tipo registro:', blank=True,choices=tipo)
	phone = models.IntegerField(verbose_name='Telefone: (campo obrigatório)')
	cidade = models.CharField(verbose_name='Cidade: (campo obrigatório)',default='none',max_length=200)
	endereco = models.CharField(max_length=254, verbose_name='Endereço:(campo obrigatório)')
	cep = models.IntegerField()
	email = models.EmailField(max_length=254,verbose_name='E-mail: (campo obrigatório)', blank=False)
	estado = models.CharField(max_length=100, choices=estado, blank=False, verbose_name='Estado: (campo obrigatório)' )
	# AO adicionar estado tive que colocar que o campo pode ser nullo pois já tem a tabela
	def __str__(self):
		return (self.nome)


class Categoria(models.Model):
	titulo = models.CharField(verbose_name='Nome:',max_length=100, blank=False)
	sub_titulo = models.CharField('Sub Titulo:',max_length=150)
	descricao = models.TextField("Descrição:")

	def __str__(self):
		return (self.titulo)

class Empreendimento(models.Model):
	titulo = models.CharField('Nome:(campo obrigatório)', max_length=200, blank=False)
	descricao = models.TextField('Descrição',blank=False)
	img = models.ImageField(verbose_name='Insira uma imagem:',blank=True, upload_to=None)
	lancamento = models.DateField('Data prevista para lançamento',blank=True, null=True)
	cat = models.ForeignKey("Categoria",verbose_name='categoria', on_delete=models.PROTECT)
	estado = models.CharField(verbose_name='Estado: (campo obrigatório)',max_length=100, choices=estado, blank=True)
	def __str__(self):
		return (self.titulo)

class Material(models.Model):
	nome = models.CharField(max_length=100,verbose_name='Nome: (campo obrigatório)', blank=False)
	descricao = models.CharField(max_length=200, blank=True)
	file = models.FileField(upload_to=None,verbose_name='Arquivos texto',blank=True)
	#testar se fica na pasta de upload
	img = models.ImageField(verbose_name='Insira uma imagem',blank=True, upload_to=None)	
	empreendimento = models.ForeignKey("Empreendimento", on_delete=models.PROTECT,)
 
	def __str__(self):
		return(self.nome)

