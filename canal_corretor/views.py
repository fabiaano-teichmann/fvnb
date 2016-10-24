from django.shortcuts import render, get_object_or_404
from .forms import AutonomoForm, ImobiliariaForm
from .models import Autonomo
from django.http import HttpResponseRedirect

def index(request):
	return render(request, 'canal_corretor/index.html', {})

def corretor_new(request):
	form = AutonomoForm(request.POST or None )
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		#depois de salvo limpa o campo nome 
		instance = form.cleaned_data.get('nome')
		#  criar um retorno. dizendo que o formulário foi enviado com sucesso
		form = AutonomoForm()
		
		return HttpResponseRedirect('/obrigado/')
	return render(request, 'canal_corretor/cad_corretor.html',{'form': form})	


def imobiliaria_new(request):
	form = ImobiliariaForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		instance = form.cleaned_data.get('razao')
		form = ImobiliariaForm()
		
		return render(request, 'canal_corretor/enviado.html')
	return render (request, 'canal_corretor/cad_imobi.html', {'form':form})	