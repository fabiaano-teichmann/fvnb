from django.db import models
from django.utils import timezone
import datetime

class Corretore(models.Model):
	nome = models.CharField(max_length=150)
	#precisa o usuário ter acesso admin
	author = models.ForeignKey ('auth.User')
	creci =  models.IntegerField()
	phone = models.IntegerField()
	cidade = models.CharField(default='none',max_length=200)
	endereco = models.CharField(max_length=254)
	cep = models.IntegerField()
	email = models.EmailField(max_length=254)
	#adicionar estado
	def __str__(self):
		return (self.nome)


class Categoria(models.Model):
	titulo = models.CharField('Titulo:',max_length=100)
	sub_titulo = models.CharField('Sub Titulo:',max_length=150)
	descricao = models.TextField("Descrição:")

	def __str__(self):
		return (self.titulo)

class Empreendimento(models.Model):
	titulo = models.CharField('Titulo:', max_length=200, blank=False)
	descricao = models.TextField(blank=False)
	img = models.ImageField(blank=True, upload_to=None)
	lancamento = models.DateTimeField('Data prevista para lançamento',blank=True, null=True)

	def __str__(self):
		return (self.titulo)

class Material(models.Model):
	nome = models.CharField(max_length=100)
	descricao = models.CharField(max_length=200)
	url = models.URLField()	
	#emreendimento = models.ForeignKey("Empreendimento", on_delete=models.CASCADE,)
 
	def __str__(self):
		return(self.nome)