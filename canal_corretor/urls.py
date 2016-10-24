from django.conf.urls import url, include , patterns
from .import views

urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^corretor/new$', views.corretor_new, name='corretor_new'),
url(r'^imobiliaria/new$', views.imobiliaria_new, name="imobiliaria_new"),
]

