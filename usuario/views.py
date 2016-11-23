from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .models import Usuario
# Create your views here.
class UsuarioView(View):

	def home(request):
		 return HttpResponse('Cadastro de usuarios')
	def usuario(request):
		form = UserModelForm(request.POST or None)
		context = {'form': form}

		if request.method =='POST':
			if form.is_valid():
				instance = form.save(commit=False)
				instance.save()
				instance = form.cleaned_data.get('username')
		return render (request, 'usuario/cadastro.html', context)

	def corretor(request):

		form = CorretorForm(request.POST or None)
		context = {'form': form}

		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			instance = form.cleaned_data.get('nome')
			#  criar um retorno. dizendo que o formulário foi enviado com sucesso
			
			return render(request, 'canal_corretor/cadastro.html')
			    #envia para prova 
		return render(request, 'canal_corretor/cad_corretor.html', context)	
