from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Noticia
# Create your views here.
def lista_noticias(request):
    noticia = Noticia.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'noticias/lista_noticias.html', {'noticia': noticia})
def post_detail(request, pk):
    post = get_object_or_404(Noticia, pk=pk)
    return render(request, 'noticias/post_detail.html', {'post': post})
def deportes(request):
    deporte = Noticia.objects.filter(categoria='DTI').order_by('fecha_publicacion')
    return render(request, 'noticias/deportes.html', {'deporte': deporte})
def entretenimiento(request):
    entretiene = Noticia.objects.filter(categoria='ER').order_by('fecha_publicacion')
    return render(request, 'noticias/entretenimiento.html', {'entretiene': entretiene})
def orden(request):
    orde = Noticia.objects.filter(categoria='OPA').order_by('fecha_publicacion')
    return render(request, 'noticias/orden.html', {'orde': orde})
def chibchombia(request):
    chibchom = Noticia.objects.filter(categoria='Ch').order_by('fecha_publicacion')
    return render(request, 'noticias/chibchombia.html', {'chibchom': chibchom})
def negocios(request):
    negocio = Noticia.objects.filter(categoria='NO').order_by('fecha_publicacion')
    return render(request, 'noticias/negocios.html', {'negocio': negocio})
