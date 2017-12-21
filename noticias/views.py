from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Noticia
from .forms import Noticia_Form
from django.contrib.auth.decorators import login_required
# Create your views here.
def lista_noticias(request):
    noticia = Noticia.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'noticias/lista_noticias.html', {'noticia': noticia})
def lista_noticias_destacadas(request):
    destaca = Noticia.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'noticias/lista_noticias.html', {'destaca': destaca})
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

def noticia_new(request):
    if request.method == "POST":
        form = Noticia_Form(request.POST, request.FILES)
        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.autor = request.user
            noticia.published_date = timezone.now()
            noticia.save()
            return redirect('post_detail', pk=noticia.pk)
    else:
        form = Noticia_Form()
    return render(request, 'noticias/form.html', {'form': form})