from django import forms
from .models import Autonomo

class AutonomoForm(forms.ModelForm):
	class Meta:
		model = Autonomo
		fields = ["nome", "nasc", "cpf", "creci", "telefone", "email", "site", "phone", "endereco", "cep" ,"cidade",  "email", "estado"]