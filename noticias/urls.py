from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
        url(r'^$', views.lista_noticias,  name='home'),
        url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
        url(r'^deportes_tropicales_de_invierno', views.deportes,  name='deportes'),
        url(r'^entretenimiento_para_robots', views.entretenimiento,  name='entretenimiento'),
        url(r'^orden_publico_alterado', views.orden,  name='orden'),
        url(r'^chibchombia', views.chibchombia,  name='chibchombia'),
        url(r'^negocios_ociosos', views.negocios,  name='negocios'),
        url(r'^noticia/new/$', login_required( views.noticia_new ), name='noticia_new'),
        url(r'^registrar', RegistroUsuario.as_view(), name = "registrar"),
]
