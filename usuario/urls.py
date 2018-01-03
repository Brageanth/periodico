from django.conf.urls import url

from usuario.views import RegistroUsuario
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^$', RegistroUsuario.as_view(), name="registrar"),
    url(r'salir$', logout, name="salira", kwargs={'next_page': '/'}),
]