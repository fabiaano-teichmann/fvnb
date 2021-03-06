from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

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


status = (
	('1', 'Pronto para Construir'),
	('2', 'Em breve'),
	('3', 'Lançado')
	)
escolha = (
	('1','a'),
	('2', 'b'),
	('3', 'c'),
	('4', 'd'),
	)
#CADASTRO DE USUÁRIOS

#CORRETOR AUTONOMO

class Corretor(models.Model):
	class Meta:
		verbose_name = 'Corretore'
	nome = models.CharField(help_text='Preencha o campo nome.',verbose_name='Nome*:',max_length=150, blank=False)
	nasc = models.DateField(verbose_name="Data de nascimento*:")
	cpf = models.CharField(verbose_name='Cpf:', blank=False, max_length=16)
	creci =  models.CharField(verbose_name='Creci Físico*:', blank=False, max_length=12)
	telefone = models.CharField(verbose_name='Telefone:', max_length=16, blank=True)
	phone = models.CharField(verbose_name='Celular:', max_length=16, blank=False)
	email = models.EmailField(max_length=254,verbose_name='E-mail*:', blank=False)
	site = models.URLField(verbose_name='site', blank=True)
	endereco = models.CharField(max_length=254, verbose_name='Endereço *:',blank=False )
	bairro = models.CharField(verbose_name='Bairro*:',max_length=100,blank=False)
	cidade = models.CharField(verbose_name='Cidade*:',blank=False,max_length=200)
	cep = models.CharField(verbose_name=' Cep*:', blank=True, max_length=16)
	estado = models.CharField(max_length=100, choices=estado, blank=False, verbose_name='Estado*:' )
	create_date = models.DateTimeField('Data de criação',default=timezone.now)
	#campo para'criar a senha para o usuário	
	def __str__(self):
		return (self.nome)

# CORRETOR LIGADO A IMOBILIARIA 

class Afiliado(models.Model):
	nome = models.CharField(verbose_name='Nome: * ',max_length=150, blank=False)
	nasc = models.DateField(verbose_name="Data de nascimento")
	cpf = models.CharField(verbose_name='CPF: * ', blank=False, max_length=16)
	creci =  models.CharField(verbose_name=' Creci Físico: * ', blank=True, max_length=12)
        #creci é opcional visto que muitas imobiliarias tem funcionarios se creci
	telefone = models.CharField(verbose_name='Telefone:*', max_length=16, blank=False)
	phone = models.CharField(verbose_name='Celular: * ', max_length=16, blank=True)
	email = models.EmailField(max_length=254,verbose_name='E-mail *: ', blank=False)
	#verificar a necessidade desse campo estar aparecendo 
	endereco = models.CharField(max_length=254, verbose_name='Endereço *:',blank=False )
	bairro = models.CharField(verbose_name='Bairro*:',max_length=100, blank=False)
	cidade = models.CharField(verbose_name='Cidade*:',blank=False,max_length=200)
	cep = models.CharField(verbose_name=' Cep*:', blank=True, max_length=16)
	estado = models.CharField(max_length=100, choices=estado, blank=False, verbose_name='Estado*:' )
	imob = models.OneToOneField("Imobiliaria", on_delete=models.CASCADE, primary_key=True, related_name="afiliado")
	create_date = models.DateTimeField('Data de criação',default=timezone.now)
	def __str__(self):
            return (self.nome)

#IMOBILIARIA

class Imobiliaria(models.Model):
    img = models.ImageField(verbose_name='Insira uma imagem:',blank=True, upload_to='static/img/imob')
    razao = models.CharField(max_length=200 ,verbose_name=' Razão social  *:', blank=False)
    creci_j = models.CharField(max_length=6, verbose_name='Creci Jurídico *:', blank=False)
    nome = models.CharField(verbose_name='Nome Fantasia *:', blank=False, max_length=150)
    cnpj = models.CharField(verbose_name=' Cnpj *:', blank=False, max_length=30)
    endereco = models.CharField(max_length=254, verbose_name='Endereço *:',blank=False )
    bairro = models.CharField(verbose_name='Bairro *: ', max_length=100, blank=True)
    cidade = models.CharField(verbose_name='Cidade *: ',blank=False,max_length=200)
    cep = models.CharField(verbose_name=' Cep *: ', blank=False, max_length=12)
    estado = models.CharField(max_length=100, choices=estado, blank=False, verbose_name='Estado*:' )
    telefone = models.CharField(verbose_name='Telefone:', max_length=16, blank=True)
    phone = models.CharField(verbose_name='Celular: ', max_length=16, blank=True)
    email = models.EmailField(max_length=254,verbose_name='E-mail *:', blank=False)
    site = models.URLField(verbose_name='site', blank=True)
    resp = models.CharField(verbose_name='Corretor Resposável*:', blank=False, max_length=150)
    email_resp = models.CharField("Email do Responsável:", max_length=200)
    cpf = models.CharField(verbose_name='CPF *: ', blank=False, max_length=16)
    creci_f =  models.CharField(verbose_name=' Creci Físico *: ', blank=True, max_length=12)
    create_date = models.DateTimeField('Data de criação',default=timezone.now)
    def __str__(self):
        return (self.nome)


#CATEGORIA

class Categoria(models.Model):
	titulo = models.CharField(verbose_name='Nome:',max_length=100, blank=False)
	img = models.ImageField(verbose_name='Insira uma imagem',blank=True, upload_to='corretor/static/img/cat')

	def __str__(self):
		return (self.titulo)

#EMPREENDIMENTOS

class Empreendimento(models.Model):
	titulo = models.CharField('Nome:(campo obrigatório)', max_length=200, blank=False)
	sub_titulo= models.CharField('Sub titulo',blank=False, max_length=150)
	descricao = models.TextField('Descrição')
	img = models.ImageField(verbose_name='Insira uma imagem:',blank=True, upload_to='static/img/empreendimento')
	lancamento = models.DateField('Data prevista para lançamento',blank=True, null=True)
	cat = models.ForeignKey("Categoria",verbose_name='categoria', on_delete=models.PROTECT, related_name="empreendimento")
	estado = models.CharField(verbose_name='Estado: (campo obrigatório)',max_length=100, choices=estado, blank=True)
	status = models.CharField('Status', max_length=30, blank=False, choices=status)
	def publish(self):
		self.lancamento = timezone.now()
		self.save()
	def __str__(self):
		return (self.titulo)

# MATERIAL DE APOIO DO CORRETOR

class Image(models.Model):
    nome = models.CharField(max_length=100,verbose_name='Nome do arquivo', blank=False)
    img = models.ImageField(verbose_name='Insira uma imagem',blank=True, upload_to='static/img/mt')
    ep_id = models.ForeignKey("Empreendimento",related_name='image', on_delete=models.PROTECT)

    def __str__(self):
        return(self.nome)
class Tabela(models.Model):
	nome = models.CharField(max_length=100,verbose_name='Nome do arquivo', blank=False)
	file = models.FileField(upload_to='static/doc',verbose_name='Arquivos ',blank=True)
	ep_id = models.ForeignKey("Empreendimento",related_name='tabela', on_delete=models.PROTECT)

	def __str__(self):
		return(self.nome)
		#não há necessidade
class Planta(models.Model):
	nome = models.CharField(max_length=100,verbose_name='Nome do arquivo', blank=False)
	file = models.FileField(upload_to='static/doc',verbose_name='Arquivos ',blank=True)
	ep_id = models.ForeignKey("Empreendimento", on_delete=models.PROTECT,related_name='planta')

	def __str__(self):
		return(self.nome)

class Material(models.Model):
	class Meta:
		verbose_name = 'Material de apoio'

	nome = models.CharField(max_length=100,verbose_name='Nome do arquivo', blank=False)
	img = models.ImageField(verbose_name='Insira uma imagem',blank=True, upload_to='static/img/ma')
	ep_id = models.ForeignKey("Empreendimento",related_name='material', on_delete=models.PROTECT)
	def __str__(self):
		return(self.nome)
class Video(models.Model):
	iframe = models.URLField(max_length=250, verbose_name='Insira iframe', blank=False)
	nome = models.CharField(max_length=100,verbose_name='Nome do arquivo', blank=False)
	ep_id = models.ForeignKey("Empreendimento", related_name="video", on_delete=models.PROTECT)

	def __str__(self):
		return(self.nome)


class Prova(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome da prova', blank=True)
    pergunta = models.CharField(max_length=200, verbose_name="Pergunta", blank=False)
    resposta = models.CharField(verbose_name='Resposta Correta',max_length=5, choices=escolha, blank=True)

    def __str__(self):
        return (self.nome)

class Pagina(models.Model):
    titulo = models.CharField('Titulo',max_length=100, blank=False )
    sub_titulo = models.CharField('Subtitulo', max_length=150, blank=False)
    nomeimg = models.CharField('Descrição da imagem', max_length=100, blank=False)
    img = models.ImageField('Banner', blank=False, upload_to='static/img/')
    descricacao = models.TextField('Descrição', blank=False)

    def __str__(self):
        return(self.titulo)






