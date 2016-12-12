from django.conf.urls import url, include , patterns
from usuario.views import UsuarioView
urlpatterns = [
	url(r'^usuario/', view.as_views()),
]