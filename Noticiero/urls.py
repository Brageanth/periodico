from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import password_reset, password_reset_done,\
    password_reset_confirm, password_reset_complete

urlpatterns = [
        url(r'^admin/', include(admin.site.urls)),
        url(r'^noticias/', include('noticias.urls')),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT
        }),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT
        }),
        url(r'^reset/password_reset$', password_reset, {'template_name':'Reset/password_reset.html', 'email_template_name':'Reset/password_reset_email.html'}, name='password_reset'),
        url(r'^reset/password_reset_done$', password_reset_done, {'template_name':'Reset/password_reset_done.html'}, name='password_reset_done'),
        url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm, {'template_name':'Reset/password_reset_confirm.html'}, name='password_reset_confirm'),
        url(r'^reset/password_reset_complete', password_reset_complete, {'template_name':'Reset/password_final.html'}, name='password_reset_complete'),
        url(r'^usuario/', include('usuario.urls', namespace='usuario')),
        url(r'', include('noticias.urls', namespace='noticias')),
]
