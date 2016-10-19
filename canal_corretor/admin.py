from django.contrib import admin
from .models import Corretore, Categoria, Empreendimento, Material
class EmpreendimentoAdmin(admin.ModelAdmin):
	save_on_top = True
	list_display = ('titulo', 'cat')
	list_filter = ('titulo', 'cat')

class MetaEmpreendimento:
	model = Empreendimento
	admin.site.register(Empreendimento, EmpreendimentoAdmin)



class CorretoreAdmin(admin.ModelAdmin):
	save_on_top = True
	list_display = ('nome', 'cidade')
	list_filter = ('nome', 'cidade')


class MetaCorretore:
	model = Corretore
	admin.site.register(Corretor, CorretorAdmin)



class CategoriaAdmin(admin.ModelAdmin):
	save_on_top = True
	list_display = ('titulo', 'sub_titulo')
	list_filter = ('titulo', 'sub_titulo')

class MetaCategoria(admin.ModelAdmin):
	model = Categoria
	admin.site.register(Categoria, CategoriaAdmin)



class MaterialAdmin(admin.ModelAdmin):
	save_on_top = True
	list_display = ('nome', 'empreendimento')
	list_filter = ('nome', 'empreendimento')


class MetaMaterial:
	
	model = Material
	admin.site.register(Material, MaterialAdmin)

# criar a classe bonitas

