from django.conf.urls import url, include , patterns
from .import views

urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^corretor_new$', views.corretor_new, name='corretor_new')

]

