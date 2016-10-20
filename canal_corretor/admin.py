from django.contrib import admin
from .models import Corretor, Imobiliaria, Autonomo, Categoria, Empreendimento, Material
# empreendimentos
class EmpreendimentoAdmin(admin.ModelAdmin):
	save_on_top = True
	list_display = ('titulo', 'cat')
	list_filter = ('titulo', 'cat')

class MetaEmpreendimento:
	model = Empreendimento
	admin.site.register(Empreendimento, EmpreendimentoAdmin)

#imobilária
class ImobiliariaAdmin(admin.ModelAdmin):
	save_on_top = True
	list_display = ('razao', 'nome', 'cidade')
	list_filter = ('razao', 'nome', 'cidade')

class MetaImobiliaria:
	model = Imobiliaria
	admin.site.register(Imobiliaria, ImobiliariaAdmin) 

# corretor
class CorretorAdmin(admin.ModelAdmin):
	save_on_top = True
	list_display = ('nome',  'vinculado')
	list_filter = ('nome', 'vinculado')


class MetaCorretor:
	model = Corretor
	admin.site.register(Corretor, CorretorAdmin)

#autonomo
class AutonomoAdmin(admin.ModelAdmin):
	save_on_top = True
	list_display = ('nome', 'cidade')
	list_filter = ('nome', 'cidade')

class MetaAutonomo:
	model = Autonomo
	admin.site.register(Autonomo, AutonomoAdmin)
#categoria
class CategoriaAdmin(admin.ModelAdmin):
	save_on_top = True
	list_display = ('titulo', 'sub_titulo')
	list_filter = ('titulo', 'sub_titulo')

class MetaCategoria(admin.ModelAdmin):
	model = Categoria
	admin.site.register(Categoria, CategoriaAdmin)


#material 
class MaterialAdmin(admin.ModelAdmin):
	save_on_top = True
	list_display = ('nome', 'empreendimento')
	list_filter = ('nome', 'empreendimento')


class MetaMaterial:
	
	model = Material
	admin.site.register(Material, MaterialAdmin)

# criar a classe bonitas

