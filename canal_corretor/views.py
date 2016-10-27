from django.shortcuts import render, get_object_or_404, redirect
from .forms import CorretorForm, ImobiliariaForm,CorretorAfiliadoForm, UserModelForm
from .models import CorretorAfiliado, Imobiliaria, Corretor
from django.http import HttpResponse
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
	return render(request, 'canal_corretor/index.html', {})

# AUTONOMO

def corretor_new(request):
	form = CorretorForm(request.POST or None)
	if form.is_valid():
		# erro 
		instance = form.save(commit=False)
		instance.save()
		#depois de salvo limpa o campo nome 
		instance = form.cleaned_data.get('nome')
		#  criar um retorno. dizendo que o formulário foi enviado com sucesso
		form = CorretorForm()
		return render(request, 'canal_corretor/enviado.html')
		
	return render(request, 'canal_corretor/cad_corretor.html',{'form': form})	

# IMOBILIARIA
@login_required
def imobiliaria_new(request):
	form = ImobiliariaForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		instance = form.cleaned_data.get('razao')
		
		# tenho que  validar consultando se o corretor já não esta cadastrado
		

		return render(request, 'canal_corretor/enviado.html')
	return render (request, 'canal_corretor/cad_imobi.html', {'form':form})	

# CORRETOR AFILIADO
@login_required
def corretorafiliado_new(request):
	
	form = CorretorAfiliadoForm(request.POST or None)
	if request.user.is_authenticated():
		if form.is_valid():
			instance = form.save(commit=False)
			instance = form.save()
			instance = form.cleaned_data.get('nome')
			
	else:	
		return redirect('/do_login')
	
	return render(request, 'canal_corretor/cad_afiliado.html', {'form':form})	

# FORMULÁRIO DE lOGIN



def do_login(request):
	if request.method =='POST':
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			login(request, user)
			return redirect('/imobiliaria/corretor/new')

	return render(request, 'canal_corretor/login.html')		


def do_logout(request):
	logout(request)
	return redirect('/login')


"""""
def cadastro(request):
	form = UserModelForm(request.POST or None)
	context = {'form': form}
	if request.method =='POST':
		if form.is_valid():
			instance = form.salve()
			instance = form.cleaned_data('username')
			

	return render (request, 'canal_corretor/cadastro.html', context)

"""
