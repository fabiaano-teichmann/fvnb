from django.forms import ModelForm
from django import forms
from .models import Corretor, Imobiliaria, CorretorAfiliado
from django.contrib.auth.models import User # importa o model da  tabela User que o django cria

#CORRETOR
class CorretorForm(forms.ModelForm):
	class Meta:
		model = Corretor
		fields = ["nome", "nasc", "cpf", "creci",
		 "telefone", "email", "site", "phone", 
		 "endereco", "cep" ,"cidade",  "email",
		  "estado"
		  ]

#IMOBILIARIA
class ImobiliariaForm(forms.ModelForm):
	class Meta:
		model = Imobiliaria
		fields = [
		"img", "razao","creci_j", "nome", "cnpj", "endereco",
		"bairro", "cidade","cep","estado", "telefone",
		"phone", "email", "site","resp", "email_resp","cpf","creci_f"

		]
		widgets = {
			'img': forms.FileInput(attrs = {'class': 'form-control'}),
			'razao':forms.TextInput(attrs ={'class': 'form-control'}),
			'creci_j': forms.TextInput(attrs ={'class': 'form-control'}),
			'nome': forms.TextInput(attrs ={'class': 'form-control'}), 
			'cnpj': forms.TextInput(attrs ={'class': 'form-control'}),
			'endereco': forms.TextInput(attrs ={'class': 'form-control'}),
			'bairro': forms.TextInput(attrs ={'class': 'form-control'}),
			'cidade': forms.TextInput(attrs ={'class': 'form-control'}),
			'cep': forms.TextInput(attrs ={'class': 'form-control'}),
			'estado': forms.Select(attrs ={'class': 'form-control'}),
			'telefone': forms.TextInput(attrs ={'class': 'form-control'}),
			'phone': forms.TextInput(attrs ={'class': 'form-control'}),
			'email': forms.EmailInput(attrs ={'class': 'form-control'}),
			'site': forms.TextInput(attrs ={'class': 'form-control'}),
			'resp': forms.TextInput(attrs ={'class': 'form-control'}),
			'email_resp': forms.EmailInput(attrs ={'class': 'form-control'}),
			'cpf': forms.TextInput(attrs ={'class': 'form-control'}),
			'creci_f': forms.TextInput(attrs ={'class': 'form-control'}),	

		}
		error_messages = {
			'razao': {'required': 'Este campo é obrigatório'},
			'creci_j': {'required': 'Este campo é obrigatório'},
			'nome': {'required': 'Este campo é obrigatório'},
			'cnpj': {'required': 'Este campo é obrigatório'},
			'endereco': {'required': 'Este campo é obrigatório'},
			'bairro': {'required': 'Este campo é obrigatório'},
			'cidade': {'required': 'Este campo é obrigatório'},
			'cep' : {'required': 'Este campo é obrigatório'},
			'estado' : {'required': 'Este campo é obrigatório'},
			'telefone': {'required': 'Este campo é obrigatório'},
			'email': {'required': 'Este campo é obrigatório'},
			'resp': {'required': 'Este campo é obrigatório'},
			'email_resp': {'required': 'Este campo é obrigatório'},
			'cpf' : {'required': 'Este campo é obrigatório'},
			

		}
#CORRETOR AFILIADO
class CorretorAfiliadoForm(forms.ModelForm):
	class Meta:
		model = CorretorAfiliado
		fields = [
		"nome","nasc", "cpf", "creci",
		 "telefone","phone", "email"
		]
		widgets = {
			'nome': forms.TextInput(attrs = {'class': 'form-control'}),
			'nasc': forms.DateInput(attrs = {'class': 'form-control' }),
			'cpf' : forms.TextInput( attrs = {'class': 'form-control'}),
			'creci': forms.TextInput(attrs= {'class': 'form-control'}),
			'telefone': forms.TextInput(attrs = {'class': 'form-control'}),
			'phone': forms.TextInput(attrs = {'class': 'form-control'}),
			'email': forms.EmailInput(attrs = {'class': 'form-control'}),				
			
		}
		error_messages ={
			'nome': {
				'required': 'Este campo é obrigatório'

			},
			'nasc': {
				'required': 'Este campo é obrigatório',
				'required': 'Digite com as 00/00/0000',
			},
			'cpf' :{
				'required': 'Este campo é obrigatório'
			},
			'creci':{
				'required': 'Este campo é obrigatório'
			},
			'telefone':{
				'required': 'Este campo é obrigatório'
			},
			'email':{
				'required': 'Este campo é obrigatório'
			},

		}	

#FORMULÁRIO DE LOGIN
class UserModelForm(forms.ModelForm):
	class Meta:
		model = User 
		fields = ['username','password']
		#janela criada para criar um form personalizado assim posso passar classe tamanho e tamanho
		widgets = {
			'username': forms.TextInput(attrs = {'class': 'form-control'}),	
			'password': forms.PasswordInput(attrs = {'class': 'form-control'}),
		}
		
		error_messages = {
			'username': {
				'required': 'Esse usuário não exite'
			},
			'password':{
				'required': 'senha Inválida'
			}
		}
