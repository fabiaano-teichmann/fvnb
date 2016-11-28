from django.shortcuts import render, get_object_or_404, redirect
from .forms import CorretorForm, ImobiliariaForm, AfiliadoForm, UserModelForm
# criar um para corretor afiliado https://www.youtube.com/watch?v=AZ1d5yEwitM&t=1718s

from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone



# FORMULÁRIO DE lOGIN
def do_login(request):
	if request.method =='POST':
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			login(request, user)
			#redireciona para a pagina de entrada
			return redirect('portal')

	return render(request, 'canal_corretor/index.html')		

"""
	PAGINA PRINCIPAL DO PORTAL
"""
@login_required
def portal(request):
	eps = Empreendimento.objects.all()
	#aplicar um filtro para que possa redirecionar 
	return render(request, 'canal_corretor/ep_list.html',{'eps': eps})



#SAÍDA DE USUÁRIO
def do_logout(request):
	logout(request)
	return redirect('login')
#Portal do corretor
@login_required


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

# CORRETOR AFILIADO
@login_required
#deferia ser uma classe protegida
def afiliado_new(request):
	# quando o formulário está vazio ele é none ou seja em branco 
	form = AfiliadoForm(request.POST or None)
	#pega os dados do formulário
	context = {'form': form}
	if not request.user.has_perm(''):
		
		if request.method == "POST":
			if form.is_valid():
				instance = form.save(commit=False)
				instance = form.save()
				instance = form.cleaned_data.get('nome')
				return render(request, 'canal_corretor/enviado.html')
	return render(request, 'canal_corretor/afiliado_new.html', context)		
		
# AUTONOMO

"""@login_required
def corretorafiliado_new(request):
	form = CorretorAfiliadoForm(request.POST or None)
	context = {}
"""
# Cadastro de corretor 
def corretor_new(request):

	form = CorretorForm(request.POST or None)
	context = {'form': form}
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		instance = form.cleaned_data.get('nome')
		#  remcaminha para criar usuario e senha
		#return redirect(cadastro)
		return redirect(ep_list)
	return render(request, 'canal_corretor/cad_corretor.html', context)

def cadastro(request):
	form = UserModelForm(request.POST or None)
	context = {'form': form}
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		#instance = form.cleaned_data.get('username')
		return redirect(corretor_new)
	return render (request, 'canal_corretor/cadastro.html', context)


# PROVA
#esperar para ver que tipo de prova
def prova(request, pk):
	form = ProvaForm(request.POST or None)
	#provas = get_object_or_404(Prova, pk=pk)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		instance = form.clearned_data.get('pergunta')
		return redirect(portal)

	return render(request, 'canal_corretor/prova.html',{'form': form})

	




#lISTAR EMPRENDIMENTOS



# DETALHAR EP

@login_required
def ep_detail(request, pk):
	emp = get_object_or_404(Empreendimento, pk=pk)
	return render(request, 'canal_corretor/ep_detail.html',{'emp': emp})

# LISTAR CATEGORIA
@login_required
def categoria(request, pk):
	cats = get_object_or_404(Categoria, pk=pk)
	eps = Empreendimento.objects.all()
	context = {
	'cats': cats,
	'eps': eps
	}

	return render(request,'canal_corretor/categoria.html',context )

# Detalhe da categoria
@login_required	
def cat_detail(request, pk):
	cats = get_object_or_404(Categoria, pk=pk)
	return render(request, 'canal_corretor/cat_detail.html', {'cats': cats})



		

