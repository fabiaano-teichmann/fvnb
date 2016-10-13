from django.contrib import admin
from .models import Corretore, Categoria, Empreendimento, Material

admin.site.register(Corretore )

admin.site.register(Categoria)

admin.site.register(Empreendimento)

class MaterialAdmin(admin.ModelAdmin):
	save_on_top = True
	list_display = ('nome', 'descricao')
	list_filter = ('nome', 'descricao')


class MetaMaterial:
	
	model = Material
	admin.site.register(Material, MaterialAdmin)

# criar a classe bonitas

