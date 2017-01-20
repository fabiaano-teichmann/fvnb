from django.conf.urls import url, include , patterns
from .import views
urlpatterns = [
# Url de login logaut e pagina principal
url (r'^logar/$',views.do_login, name="do_login"),
url(r'^$', views.do_login, name="login"),# pagina index do site onde o usúario se loga e tem link para cadastrar
url(r'^logout/$', views.do_logout, name="logout"), # pagina de saida de ususárip
#cadatros
url(r'^cadastro/$', views.cadastro, name="cadastro"), # cadastro do usuário e senha
url(r'^corretor/new$', views.corretor_new, name='corretor_new'),# cadastro dos dados dos usuários
url(r'^imobiliaria/new$', views.imobiliaria_new, name="imobiliaria_new"),# cadastro de imobiliarias
url(r'^imobiliaria/corretor/new$', views.afiliado_new, name="afiliado_new"), # corretores afiliados que se cadastrarm no site
#visualização de empreendimentos
#url(r'^categorias/(?P<pk>[0-9]+)/$', views.categoria, name="categoria"), # lista as categorias do 
url(r'^portal/$', views.portal, name="portal"), # portal do site é a página de boas vindas e lista os empreendimentos
url(r'^categorias/$', views.cat_detail, name="cat_detail"),
url(r'^lista/categorias/$', views.cat_list, name="cat_list"
url(r'^detalhes/empreendimento/(?P<pk>[0-9]+)/$', views.ep_detail, name="ep_detail"), #mostra o emprendimentos com todos detalhes
url(r'^prova/(?P<pk>[0-9]+)/$', views.prova, name="prova"),# prova para corretor de 

]


