from django.forms import ModelForm
from django import forms
from .models import Corretor, Imobiliaria, CorretorAfiliado
from django.contrib.auth.models import User # importa o model da  tabela User que o django cria

#CORRETOR AUTONOMO 
class CorretorForm(forms.ModelForm):
	class Meta:
		model = Corretor
		fields = ["nome", "nasc", "cpf", "creci",
		 "telefone", "email", "site", "phone", 
		 "endereco", "cep" ,"cidade",  "email",
		 "estado"
		  ]
		widgets = {
			"nome":forms.TextInput(attrs ={'class': 'form-control fvnb', 'placeholder': 'Nome'}),
		  	"nasc" :forms.DateInput(attrs ={'class': 'form-control fvnb','placeholder': 'Data Nascimento'}),
		  	"cpf"	:forms.TextInput(attrs ={'class': 'form-control fvnb', 'placeholder': 'CPF'}),
		  	"creci" :forms.TextInput(attrs ={'class': 'form-control fvnb', 'placeholder': 'Creci'}),
		  	"telefone" :forms.TextInput(attrs ={'class': 'form-control fvnb', 'placeholder': 'Telefone'}),
		  	"email" :forms.TextInput(attrs ={'class': 'form-control fvnb', 'placeholder': 'E-mail'}),
		  	"site" :forms.URLInput(attrs ={'class': 'form-control fvnb', 'placeholder': 'Site'}),
		  	"phone" :forms.TextInput(attrs ={'class': 'form-control fvnb', 'placeholder': 'Celular'}),
		  	"endereco":forms.TextInput(attrs ={'class': 'form-control fvnb', 'placeholder': 'Endereço'}),
		  	"cep" :forms.TextInput(attrs ={'class': 'form-control fvnb', 'placeholder': 'Cep'}),
		  	"cidade" :forms.TextInput(attrs ={'class': 'form-control fvnb', 'placeholder': 'Cidade'}),
		  	"estado":forms.Select(attrs ={'class': 'form-control fvnb', 'placeholder': 'Estado'}),
		  }
		error_messages = { 
			'nome': {'required': 'Este campo é obrigatório'},
			'nasc': {'required': 'Este campo é obrigatório'},
			'cpf': {'required': 'Este campo é obrigatório'},
			'creci': {'required': 'Este campo é obrigatório'},
			'email': {'required': 'Este campo é obrigatório'},
			'phone': {'required': 'Este campo é obrigatório'},
			'endereco': {'required': 'Este campo é obrigatório'},
			'cidade': {'required': 'Este campo é obrigatório'},
			'estado': {'required': 'Este campo é obrigatório'},

		  }



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
			'img': forms.FileInput(attrs = {'class': 'form-control', 'placeholder': 'Imagem'}),
			'razao':forms.TextInput(attrs ={'class': 'form-control', 'placeholder': 'Razão social'}),
			'creci_j': forms.TextInput(attrs ={'class': 'form-control','placeholder': 'Creci Jurídico'}),
			'nome': forms.TextInput(attrs ={'class': 'form-control','placeholder': 'Nome'}), 
			'cnpj': forms.TextInput(attrs ={'class': 'form-control','placeholder': 'Cnpj'}),
			'endereco': forms.TextInput(attrs ={'class': 'form-control', 'placeholder': 'Endereço'}),
			'bairro': forms.TextInput(attrs ={'class': 'form-control','placeholder': 'Bairro'}),
			'cidade': forms.TextInput(attrs ={'class': 'form-control','placeholder': 'Cidade'}),
			'cep': forms.TextInput(attrs ={'class': 'form-control', 'placeholder': 'Cep'}),
			'estado': forms.Select(attrs ={'class': 'form-control', 'placeholder': 'Estado' }),
			'telefone': forms.TextInput(attrs ={'class': 'form-control', 'placeholder': 'Telefone'}),
			'phone': forms.TextInput(attrs ={'class': 'form-control', 'placeholder': 'Celular'}),
			'email': forms.EmailInput(attrs ={'class': 'form-control', 'placeholder': 'E-mail' }),
			'site': forms.TextInput(attrs ={'class': 'form-control', 'placeholder': 'Site'}),
			'resp': forms.TextInput(attrs ={'class': 'form-control', 'placeholder': 'Responsável'}),
			'email_resp': forms.EmailInput(attrs ={'class': 'form-control' , 'placeholder': 'E-mail responsável'}),
			'cpf': forms.TextInput(attrs ={'class': 'form-control' , 'placeholder': 'Cpf'}),
			'creci_f': forms.TextInput(attrs ={'class': 'form-control' , 'placeholder': 'Creci Físico'}),	

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
		 "telefone","phone", "email","endereco", "cidade", "estado"
		]
		widgets = {
			'nome': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Nome'}),
			'nasc': forms.DateInput(attrs = {'class': 'form-control', 'placeholder':'Data Nascimento' }),
			'cpf' : forms.TextInput( attrs = {'class': 'form-control',  'placeholder': 'Cpf'}),
			'creci': forms.TextInput(attrs= {'class': 'form-control' , 'placeholder': 'Creci'}),
			'telefone': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Telefone'}),
			'phone': forms.TextInput(attrs = {'class': 'form-control' , 'placeholder': 'Celular'}),
			'email': forms.EmailInput(attrs = {'class': 'form-control' , 'placeholder': 'E-mail'}),				
			"endereco":forms.TextInput(attrs ={'class': 'form-control', 'placeholder': 'Endereço'}),
		  	"cidade" :forms.TextInput(attrs ={'class': 'form-control', 'placeholder': 'Cidade'}),
		  	"estado":forms.Select(attrs ={'class': 'form-control', 'placeholder': 'Estado'}),

		  	# ver documentação completa do form e perguntar em forum
		  	#"id_imob": forms.Select(attrs={'class':'form-contrl', 'placeholder': 'imobiliaria'}),
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
			'endereco': {
				'required': 'Este campo é obrigatório'
				},
			'bairro': {
				'required': 'Este campo é obrigatório'
				},
			'cidade': {
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
