from django import forms
from .models import Autonomo, Imobiliaria

class AutonomoForm(forms.ModelForm):
	class Meta:
		model = Autonomo
		fields = ["nome", "nasc", "cpf", "creci", "telefone", "email", "site", "phone", "endereco", "cep" ,"cidade",  "email", "estado"]

class ImobiliariaForm(forms.ModelForm):
	class Meta:
		model = Imobiliaria
		fields = [
		"img", "razao", "nome", "cnpj", "endereco",
		"bairro", "cidade","cep","estado", "telefone",
		"phone", "email", "site", "email_resp","cpf","creci_f"

		]
