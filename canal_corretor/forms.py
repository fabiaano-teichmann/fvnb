from django import forms
from .models import Corretore

class CorretoreForm(forms.ModelForm):
	class Meta:
		model = Corretore
		fields = ["nome", "creci", "tipo","phone", "endereco", "cep" ,"cidade",  "email", "estado"]