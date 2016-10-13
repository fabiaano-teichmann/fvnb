from django.contrib import admin
from .models import Corretor, Categoria, Empreendimento, Material
class EmpreendimentoAdmin(admin.ModelAdmin):
	save_on_top = True
	list_display = ('titulo', 'lancamento')
	list_filter = ('titulo', 'lancamento')

class MetaEmpreendimento:
	model = Empreendimento
	admin.site.register(Empreendimento, EmpreendimentoAdmin)



class CorretorAdmin(admin.ModelAdmin):
	save_on_top = True
	list_display = ('nome', 'cidade')
	list_filter = ('nome', 'cidade')


class MetaCorretor:
	model = Corretor
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
	list_display = ('nome', 'descricao')
	list_filter = ('nome', 'descricao')


class MetaMaterial:
	
	model = Material
	admin.site.register(Material, MaterialAdmin)

# criar a classe bonitas

