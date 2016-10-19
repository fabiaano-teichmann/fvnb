from django import forms
from .models import Corretor

class CorretorForm(forms.ModelForm):
	class Meta:
		model = Corretor
		fields = ["nome", "creci", "phone", "endereco", "cep" ,"cidade",  "email", "estado"]