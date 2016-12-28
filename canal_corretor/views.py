from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import menssages
from .forms import CorretorForm, ImobiliariaForm, AfiliadoForm, UserModelForm
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone



# FORMULÁRIO DE lOGIN
#essa página é a pagina inicial onde tem o acesso de login e onde as imobiliarias e os corretores podem se cadastrar,

def do_login(request):
    if request.method =='POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            #redireciona para a pagina de entrada
            return redirect('portal')
    return render(request, 'canal_corretor/index.html')
"""
def teste(request):
    if request.method = 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not  None:
            login(request, user)
            return redirect('portal')
    return render(request, ='canal_corretor/index.htm')
"""
"""
Essa pagina o usuário depois de se locar entra e visualizar os empreendimentos abertos .
"""
@login_required
def portal(request):
    eps = Empreendimento.objects.all()
     #aplicar um filtro para que possa redirecionar 
    return render(request, 'canal_corretor/ep_list.html',{'eps': eps} )


#SAÍDA DE USUÁRIO
def do_logout(request):
    logout(request)
    return redirect(login)


# IMOBILIARIA

def imobiliaria_new(request):
    # Pega a classe form
    form = ImobiliariaForm(request.POST or None)
    # AQUI A VALIDAÇÃO DOS CAMPOS SÃO FEITA O QUE TENHO QUE FAZER E ENVIAR UMA MENSAGEM DE ERRO
    if form.is_valid():
        instance = form.save(commit=False)
        instance = form.save()
        #salva o  formulário e limpa o campo razão social
        instance = form.cleaned_data.get('razao')
	# tenho que  validar consultando se o corretor já não esta cadastrado
        return redirect(cadastro)
    return render (request, 'canal_corretor/cad_imobi.html', {'form':form})

# CORRETOR AFILIADO
@login_required
#decorador do django que tem é uma função que chama outra função
def afiliado_new(request):
    # quando o formulário está vazio ele é none ou seja em branco 
    form = AfiliadoForm(request.POST or None)
    #pega os dados do formulário
    context = {'form': form}
    #if not request.user.has_perm(''):
        #verifica se o usuário possui permissão para fazer essa alteração já que o usuário tem que estar logado e ter permisão de imobiliaria
    if form.is_valid():
        #instanc recebe o form com as função de save e de limpar campo do formulário
        instance = form.save(commit=False)
        instance = form.save()
        instance = form.cleaned_data.get('nome')
        return redirect(cadastro)
    return render(request, 'canal_corretor/afiliado_new.html', context)


# CADASTRO DE CORRETORES DEPPOIS DE CADASTRADO EMCAMINHA PARA CRIAR SENHA 
def corretor_new(request):
    form = CorretorForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance = form.save()
        instance = form.cleaned_data.get('nasc')
        return redirect(cadastro)
    return render(request, 'canal_corretor/cad_corretor.html',{'form': form})

def cadastro(request):
    form = UserModelForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        instance = form.save(commit=False)
        instance = form.save()
        instance = form.cleaned_data.get('username')
        return redirect(portal)
    return render(request, 'canal_corretor/cadastro.html', context)


# PROVA
#esperar para ver que tipo de prova
def prova(request, pk):
    form = ProvaForm(request.POST or None)
    #provas = get_object_or_404(Prova, pk=pk)
    if form.is_valid():
        instance = form.save(commit=False)
        instance = form.save()
        instance = form.clearned_data.get('pergunta')
        return redirect(portal)
    return render(request, 'canal_corretor/prova.html',{'form': form})


#lISTAR EMPRENDIMENTOS



# DETALHAR EP

@login_required
def ep_detail(request, pk):
    eps = get_object_or_404(Empreendimento, pk=pk)
    return render(request, 'canal_corretor/ep_detail.html',{'eps': eps})

# LISTAR CATEGORIA
@login_required
def categoria(request, pk):
    cats = get_object_or_404(Categoria, pk=pk)
    context = {
	'cats': cats }
    return render(request,'canal_corretor/categoria.html',context )
# LISTA AS CATEGORIAS DOS EMPREENDIMENTOS
@login_required
def cat_ep(request):
    cats = Categoria.object.all()
    context = {'cats': cats}
    return render(request, 'canal_corretor/cat_ep.html', context)










