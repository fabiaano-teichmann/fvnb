from django.shortcuts import render, get_object_or_404
from .forms import CorretorForm, ImobiliariaForm,CorretorAfiliadoForm
from .models import CorretorAfiliado, Imobiliaria, Corretor
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm # Formulario de criacao de usuarios

def index(request):
	return render(request, 'canal_corretor/index.html', {})
# AUTONOMO

def corretor_new(request):
	form = AutonomoForm(request.POST or None)
	if form.is_valid():
		# erro 
		instance = form.save(commit=False)
		instance.save()
		#depois de salvo limpa o campo nome 
		instance = form.cleaned_data.get('nome')
		#  criar um retorno. dizendo que o formulário foi enviado com sucesso
		form = AutonomoForm()
		return render(request, 'canal_corretor/enviado.html')
		
	return render(request, 'canal_corretor/cad_corretor.html',{'form': form})	
# IMOBILIARIA

def imobiliaria_new(request):
	form = ImobiliariaForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		instance = form.cleaned_data.get('razao')
		
		# tenho que  validar consultando se o corretor já não esta cadastrado
		

		return render(request, 'canal_corretor/enviado.html')
	return render (request, 'canal_corretor/cad_imobi.html', {'form':form})	

# CORRETOR
def corretorafiliado_new(request):
	if request.user.is_authenticated():
		return render (request, 'canal_corretor/cad_afiliado.html')

	else:	
		return HttpResponse("<h1> Se logue no sistema </h1>")