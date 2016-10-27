from django.db import models
from django.utils import timezone
import datetime
estado = (
	('AC','Acre' ),
	('AL','Alagoas'),
	('AP','Amapá'),
	('AM','Amazonas'),
	('BA','Bahia'),
	('CE','Ceará'),
	('DF','Distrito Federal'),
	('ES','Espírito Santo'),
	('GO', 'Goiás'),
	('MA', 'Maranhão'),
	('MT', 'Mato Grosso'),
	('MS', 'Mato Grosso do Sul'),
	('MG', 'Minas Gerais'),
	('PA', 'Pará'),
	('PB', 'Paraíba'),
	('PR','Paraná' ),
	('PE','Pernambuco'),
	('PI', 'Piauí'),
	('RJ', 'Rio de Janeiro'),
	('RN', 'Rio Grande do Norte'),
	('RS', 'Rio Grande do Sul'),
	('RO', 'Rondônia'),
	('RR', 'Roraima'),
	('SC','Santa Catarina'),
	('São Paulo', 'SP'),
	('SE', 'Sergipe'),
	('TO', 'Tocantins'),
	)

status_user = (
	('1','Inativo'),
	('2','Ativo'),
	)
#CADASTRO DE USUÁRIOS

#CORRETOR AUTONOMO

class Corretor(models.Model):
	nome = models.CharField(verbose_name='Nome*:',max_length=150, blank=False)
	nasc = models.DateField(verbose_name="Data de nascimento*:")
	cpf = models.CharField(verbose_name='Cpf:', blank=False, max_length=16)
	creci =  models.CharField(verbose_name='Creci Físico*:', blank=False, max_length=12)
	telefone = models.CharField(verbose_name='Telefone:', max_length=16, blank=False)
	phone = models.CharField(verbose_name='Celular:', max_length=16, blank=True)
	email = models.EmailField(max_length=254,verbose_name='E-mail*:', blank=False)
	site = models.URLField(verbose_name='site', blank=True)
	endereco = models.CharField(max_length=254, verbose_name='Endereço *:',blank=False )
	bairro = models.CharField(verbose_name='Bairro*:',max_length=100,blank=False)
	cidade = models.CharField(verbose_name='Cidade*:',blank=False,max_length=200)
	cep = models.CharField(verbose_name=' Cep*:', blank=False, max_length=16)
	estado = models.CharField(max_length=100, choices=estado, blank=False, verbose_name='Estado*:' )
	ativacao = models.CharField(max_length=10, choices=status_user, blank=True, default=1) 
	create_date = models.DateTimeField('Data de criação',default=timezone.now)
	#campo para'criar a senha para o usuário 
	
	def __str__(self):
		return (self.nome)

# CORRETOR LIGADO A IMOBILIARIA 

class CorretorAfiliado(models.Model):
	nome = models.CharField(verbose_name='Nome: * ',max_length=150, blank=False)
	nasc = models.DateField(verbose_name="Data de nascimento")
	cpf = models.CharField(verbose_name='CPF: * ', blank=False, max_length=16)
	creci =  models.CharField(verbose_name=' Creci Físico: * ', blank=False, max_length=12)
	telefone = models.CharField(verbose_name='Telefone:*', max_length=16, blank=False)
	phone = models.CharField(verbose_name='Celular: * ', max_length=16, blank=True)
	email = models.EmailField(max_length=254,verbose_name='E-mail *: ', blank=False)
	#verificar a necessidade desse campo estar aparecendo 
	vinculado = models.ForeignKey("Imobiliaria",verbose_name='Imobiliária vinculada', on_delete=models.CASCADE)
	create_date = models.DateTimeField('Data de criação',default=timezone.now)
	#pedir os campos obrigátórios e se é só numero ou se é com caracter
	# pegar a chave estrangeira de imobiliaria
		
	
	def __str__(self):
		return (self.nome)

#IMOBILIARIA

class Imobiliaria(models.Model):
	img = models.ImageField(verbose_name='Insira uma imagem:',blank=True, upload_to=None)
	razao = models.CharField(max_length=200 ,verbose_name=' Razão social  *:', blank=False)
	creci_j = models.CharField(max_length=6, verbose_name='Creci Jurídico *:', blank=False)
	nome = models.CharField(verbose_name='Nome Fantasia *:', blank=False, max_length=150)
	cnpj = models.CharField(verbose_name=' Cnpj *:', blank=False, max_length=14)
	endereco = models.CharField(max_length=254, verbose_name='Endereço *:',blank=False )
	bairro = models.CharField(verbose_name='Bairro *: ', max_length=100, blank=True)
	cidade = models.CharField(verbose_name='Cidade *: ',blank=False,max_length=200)
	cep = models.CharField(verbose_name=' Cep *: ', blank=False, max_length=12)
	estado = models.CharField(max_length=100, choices=estado, blank=False, verbose_name='Estado *:' )	
	telefone = models.CharField(verbose_name='Telefone:', max_length=16, blank=True)
	phone = models.CharField(verbose_name='Celular: ', max_length=16, blank=True)
	email = models.EmailField(max_length=254,verbose_name='E-mail *:', blank=False)
	site = models.URLField(verbose_name='site', blank=True)
	resp = models.CharField(verbose_name='Corretor Resposável *:', blank=False, max_length=150)
	email_resp = models.CharField("Email do Responsável:", max_length=200)
	cpf = models.CharField(verbose_name='CPF *: ', blank=False, max_length=16)
	creci_f =  models.CharField(verbose_name=' Creci Físico *: ', blank=False, max_length=12)
	ativacao = models.CharField(max_length=10, choices=status_user, blank=True, default=1)
	create_date = models.DateTimeField('Data de criação',default=timezone.now)
	def __str__(self):
		return (self.nome)

#PARTE DE CADASTRO DOS EMPREENDIMENTOS NB


#CATEGORIA

class Categoria(models.Model):
	titulo = models.CharField(verbose_name='Nome:',max_length=100, blank=False)
	sub_titulo = models.CharField('Sub Titulo:',max_length=150)
	

	def __str__(self):
		return (self.titulo)

#EMPREENDIMENTOS

class Empreendimento(models.Model):
	titulo = models.CharField('Nome:(campo obrigatório)', max_length=200, blank=False)
	descricao = models.TextField('Descrição',blank=False)
	img = models.ImageField(verbose_name='Insira uma imagem:',blank=True, upload_to=None)
	lancamento = models.DateField('Data prevista para lançamento',blank=True, null=True)
	cat = models.ForeignKey("Categoria",verbose_name='categoria', on_delete=models.PROTECT)
	estado = models.CharField(verbose_name='Estado: (campo obrigatório)',max_length=100, choices=estado, blank=True)
	def __str__(self):
		return (self.titulo)

#MATERIAL DE APOIO DO CORRETOR

class Material(models.Model):
	nome = models.CharField(max_length=100,verbose_name='Nome: (campo obrigatório)', blank=False)
	descricao = models.CharField(max_length=200, blank=True)
	file = models.FileField(upload_to=None,verbose_name='Arquivos texto',blank=True)
	#testar se fica na pasta de upload
	img = models.ImageField(verbose_name='Insira uma imagem',blank=True, upload_to=None)	
	empreendimento = models.ForeignKey("Empreendimento", on_delete=models.PROTECT,)
 
	def __str__(self):
		return(self.nome)

# EMAIL MARKETING




