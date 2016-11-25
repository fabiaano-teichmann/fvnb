from django.forms import ModelForm
from django import forms
from .models import Corretor, Imobiliaria, Afiliado, Prova
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
		#email = forms.ModelChoiceField(queryset=User.objects.all().order_by('id'), widget=forms.Select({'class': 'form-control' })),
		#id_cargo = forms.ModelChoiceField (queryset=Cargo.objects.all().order_by('id'), widget=forms.Select)
		widgets = {
			"nome":forms.TextInput(attrs ={'class': 'form-control ', 'placeholder': 'Nome'}),
		  	"nasc" :forms.DateInput(attrs ={'class': 'form-control ','placeholder': 'Data Nascimento'}),
		  	"cpf"	:forms.TextInput(attrs ={'class': 'form-control ', 'placeholder': 'CPF'}),
		  	"creci" :forms.TextInput(attrs ={'class': 'form-control ', 'placeholder': 'Creci'}),
		  	"telefone" :forms.TextInput(attrs ={'class': 'form-control ', 'placeholder': 'Telefone'}),
		  	"email" :forms.TextInput(attrs ={'class': 'form-control ', 'placeholder': 'E-mail'}),
		  	#"email": forms.ModelChoiceField(queryset=User.objects.all().order_by('id'), widget=forms.Select(attrs ={'class': 'form-control ', 'placeholder': 'Email'})),
		  	"site" :forms.URLInput(attrs ={'class': 'form-control ', 'placeholder': 'Site'}),
		  	"phone" :forms.TextInput(attrs ={'class': 'form-control ', 'placeholder': 'Celular'}),
		  	"endereco":forms.TextInput(attrs ={'class': 'form-control', 'placeholder': 'Endereço'}),
		  	"cep" :forms.TextInput(attrs ={'class': 'form-control ', 'placeholder': 'Cep'}),
		  	"cidade" :forms.TextInput(attrs ={'class': 'form-control ', 'placeholder': 'Cidade'}),
		  	"estado":forms.Select(attrs ={'class': 'form-control ', 'placeholder': 'Estado'}),
		  	
		  }
		 
		error_messages = { 
			'nome': {'required': 'Este campo é obrigatório'},
			'nasc': {'required': 'Este campo é obrigatório'},
			'cpf': {'required': 'Este campo é obrigatório'},
			'creci': {'required': 'Este campo é obrigatório'},
			'email': {'Requer': 'O uso de @ e .'},
			'phone': {'required': 'Este campo é obrigatório'},
			'endereco': {'required': 'Este campo é obrigatório'},
			'cidade': {'required': 'Este campo é obrigatório'},
			'estado': {'required': 'Este campo é obrigatório'},

			}
			#1784848Ab@$1sdgsA
	

class ProvaForm(forms.ModelForm):
	class Meta:
		model = Prova
		fields = ['resposta']
		widgets = {
			
			'resposta': forms.RadioSelect(attrs = {'class': 'form-control', 'placeholder': 'Resposta'}),
		}


class UserModelForm(forms.ModelForm):
	class Meta:
		model = User 
		fields = ['username','email', 'password']
		#janela criada para criar um form personalizado assim posso passar classe tamanho e tamanho
		widgets = {
			'username': forms.TextInput(attrs = {'class': 'form-control','placeholder': 'Nome de usuário'}),
			'email': forms.EmailInput(attrs = {'class': 'form-control', 'placeholder': 'E-mail caso precise redefinir senha'}),			
			'password': forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder': 'Senha'}),
			
			
		}
		
		error_messages = {
			'username': {'required': 'Esse usuário não exite'},
			'email': {'Required': 'Email tem que possuir @'},
			'password':{ 'required': 'senha Inválida'},

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

class AfiliadoForm(forms.ModelForm):
	class Meta:
		model = Afiliado
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


# Formulário de cadastro de usuário

