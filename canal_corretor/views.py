from django.shortcuts import render, get_object_or_404, redirect
from .forms import CorretorForm, ImobiliariaForm,CorretorAfiliadoForm, UserModelForm
from .models import CorretorAfiliado, Imobiliaria, Corretor, Empreendimento, Categoria
from django.http import HttpResponse
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone


@login_required
def index (request):
	if request.user.is_authenticated():
		cats = Categoria.objects.all()
		return render(request, 'canal_corretor/index.html', {'cats': cats})
	else:
		return redirect('/do_login')	


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
			print(form)
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
#lISTAR EPRENDIMENTOS
def ep_list(request):
	eps = Empreendimento.objects.filter(lancamento=timezone.now()).order_by()
	#aplicar um filtro para que possa redirecionar 
	return render(request, 'canal_corretor/ep_list.html',{'eps': eps})

# LISTAR CATEGORIA
"""
def cat_list(request):
	cat = Categoria.objects.all()
	return render 

"""	
# DETALHAR EP
@login_required
def ep_detail(request):
	if request.user.is_authenticated():
		eps = get_object_or_404(Empreendimento, pk=pk)
		return render(request, 'canal_corretor/ep_detail.html',{'eps': eps})
	else:
		return redirect('/do_login')	

# CATEGORIAS

