from django.shortcuts import render, get_object_or_404
from .forms import AutonomoForm
from .models import Autonomo
# Create your views here.

def index(request):
	return render(request, 'canal_corretor/index.html', {})

def corretor_new(request):
	
	#if request.method == "POST":
	#	print ( "nome: " + request.POST.get("nome"))
	#	print ( " cidade:" + request.POST.get("cidade"))
		#print (request.POST.get("email"))
		#print (request.POST.get("estado"))
		#Post.object.create("nome")
	form = AutonomoForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		
	return render(request, 'canal_corretor/cad_corretor.html',{'form': form})
