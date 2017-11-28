from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
        url(r'^admin/', include(admin.site.urls)),
        url(r'', include('noticias.urls')),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT
        }),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT
        }), 
]
