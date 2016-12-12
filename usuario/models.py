from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Usuario():
	nome = models.CharField('Nome', blank=False, max_length=100)
	email = models.EmailField('E-mail', max_length=150, blank=False)
	senha = models.CharField('Senha', max_length=150)
 
	def __str(self):
		return(self.nome)