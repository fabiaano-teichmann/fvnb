from django.forms import ModelForm
from django import forms
from .models import Corretor, Imobiliaria, Afiliado, Prova
from django.contrib.auth.models import User # importa o model da  tabela User que o django cria
from django.core.exceptions import ValidationError
#CORRETOR 
class CorretorForm(forms.ModelForm):

    class Meta:
        model = Corretor
        fields = ['nome', 'nasc', 'cpf', 'creci', 'telefone', 'phone', 'email', 'site', 'endereco', 'bairro','cep', 'cidade', 'estado']  
        widgets = {
            'nome':forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Nome'}),
            'nasc': forms.DateInput(attrs = {'class': 'form-control', 'placeholder':'Data Nascimento' }),
            'cpf' : forms.TextInput( attrs = {'class': 'form-control',  'placeholder': 'Cpf'}),
            'creci': forms.TextInput(attrs= {'class': 'form-control' , 'placeholder': 'Creci'}),
            'telefone': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Telefone'}),
            'phone': forms.TextInput(attrs = {'class': 'form-control' , 'placeholder': 'Celular'}),
            'email': forms.EmailInput(attrs = {'class': 'form-control' , 'placeholder': 'E-mail'}),
            'endereco':forms.TextInput(attrs ={'class': 'form-control', 'placeholder': 'Endereço'}),
            'bairro' :forms.TextInput(attrs = {'class':'form-control', 'placeholder': 'Bairro'}),
            'cidade' :forms.TextInput(attrs ={'class': 'form-control', 'placeholder': 'Cidade'}),
            'cep': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Cep'}),
            'estado': forms.Select(attrs ={'class': 'form-control', 'placeholder': 'Estado'}),
            'site': forms.TextInput(attrs ={' class': 'form-control', 'placeholder': 'Site'}),
            }

        def clean_nome(self):
            nome = self.cleaned_data['nome']
            if len(nome) < 10:
                raise forms.ValidationError('Digite seu nome completo')
            return (nome)

        def clean_cpf(self):
            cpf = self.cleaned_data['cpf']
            if len(cpf) < 10:
                raise forms.ValidationError('Digite seu cpf')
            return (cpf)

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
            'email': {'Required': 'Email tem que possuir @ e ponto'},
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
            def clean_razao(self):
                razao = self.cleaned_data['nome']
                if len(razao) < 10:
                    raise forms.ValidationError('Digite seu nome completo')
                return (razao)
            def clean_telefone(self):
                telefone = self.cleaned_data['telefone']
                if len(telefone) > 10:
                    raise forms.ValidationError('Seu telefone não preenchido corretamente')
                return(telefone)


#PROVA PARA CORRETORES
class ProvaForm(forms.ModelForm):
	class Meta:
		model = Prova
		fields = ['resposta']
		widgets = {

			'resposta': forms.RadioSelect(attrs = {'class': 'form-control', 'placeholder': 'Resposta'}),
		}


#CORRETOR AFILIADO

class AfiliadoForm(forms.ModelForm):

    class Meta:
        model = Afiliado
        fields = [ "nome","nasc", "cpf", "creci","telefone","phone", "email","endereco","bairro", "cidade","cep", "estado", "imob"]
        widgets = {
            'nome': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Nome'}),
            'nasc': forms.DateInput(attrs = {'class': 'form-control', 'placeholder':'Data Nascimento' }),
            'cpf' : forms.TextInput( attrs = {'class': 'form-control',  'placeholder': 'Cpf'}),
            'creci': forms.TextInput(attrs= {'class': 'form-control' , 'placeholder': 'Creci'}),
            'telefone': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Telefone'}),
            'phone': forms.TextInput(attrs = {'class': 'form-control' , 'placeholder': 'Celular'}),
            'email': forms.EmailInput(attrs = {'class': 'form-control' , 'placeholder': 'E-mail'}),
            'endereco':forms.TextInput(attrs ={'class': 'form-control', 'placeholder': 'Endereço'}),
            'bairro' :forms.TextInput(attrs = {'class':'form-control', 'placeholder': 'Bairro'}),
            'cidade' :forms.TextInput(attrs ={'class': 'form-control', 'placeholder': 'Cidade'}),
            'cep' : forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Cep'}),
            'estado':forms.Select(attrs ={'class': 'form-control', 'placeholder': 'Estado'}),
            'imob': forms.Select(attrs={'class':'form-control', 'placeholder': 'imobiliaria'}),
	}
        error_messages ={
            'nome': {'required': 'Este campo é obrigatório'},
            'nasc': {'required': 'Digite com as 00/00/0000',},
            'cpf' :{'required': 'Este campo é obrigatório'},
            'creci':{'required': 'Este campo é obrigatório'},
            'telefone':{'required': 'Este campo é obrigatório'},
            'email':{'required': 'Este campo é obrigatório'},
            'endereco': {'required': 'Este campo é obrigatório'	},
            'bairro': {'required': 'Este campo é obrigatório'},
            'cidade': {	'required': 'Este campo é obrigatório'	},
            'imob':{ 'required': 'Este campo é requirido' },


         }
