from django.conf.urls import url

from usuario.views import RegistroUsuario

urlpatterns = [
    url(r'^$', RegistroUsuario.as_view(), name="registrar"),
]