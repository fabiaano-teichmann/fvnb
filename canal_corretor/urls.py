from django.conf.urls import url, include , patterns
from .import views

urlpatterns = [
# Url de login logaut e pagina principal
url(r'^$', views.do_login, name="login"),
url(r'^logout/$', views.do_logout, name="logout"),
url(r'^portal/$', views.portal, name="portal"),
#cadatros
url(r'^cadastro/$', views.cadastro, name="cadastro"),
url(r'^corretor/new$', views.corretor_new, name='corretor_new'),
url(r'^imobiliaria/new$', views.imobiliaria_new, name="imobiliaria_new"),
url(r'^imobiliaria/corretor/new$', views.afiliado_new, name="afiliado_new"),
#visualização de empreendimentos
url(r'^categorias/(?P<pk>[0-9]+)/$', views.categoria, name="categoria"),
url(r'^detalhes/empreendimento/(?P<pk>[0-9]+)/$', views.ep_detail, name="ep_detail"),
url(r'^prova/(?P<pk>[0-9]+)/$', views.prova, name="prova"),

]


