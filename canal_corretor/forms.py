from django import forms
from .models import Corretor, Imobiliaria, CorretorAfiliado

class CorretorForm(forms.ModelForm):
	class Meta:
		model = Corretor
		fields = ["nome", "nasc", "cpf", "creci",
		 "telefone", "email", "site", "phone", 
		 "endereco", "cep" ,"cidade",  "email",
		  "estado"
		  ]

#Imobiliaria
class ImobiliariaForm(forms.ModelForm):
	class Meta:
		model = Imobiliaria
		fields = [
		"img", "razao", "nome", "cnpj", "endereco",
		"bairro", "cidade","cep","estado", "telefone",
		"phone", "email", "site", "email_resp","cpf","creci_f"

		]
class CorretorAfiliadoForm(forms.ModelForm):
	class Meta:
		model = CorretorAfiliado
		fields = [
		"nome","nasc", "cpf", "creci",
		 "telefone","phone", "email", "vinculado"
		]


		