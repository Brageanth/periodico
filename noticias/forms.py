from django import forms
from .models import Noticia

class Noticia_Form(forms.ModelForm):
    
    class Meta:
        model=Noticia
        fields = [
                'titulo',
                'encabezado',
                'texto',
                'imagen',
                'categoria',
            ]
        
        # Este es el arreglo con las etiquetas para cada uno de los campos que
        # usaremos
        labels = {
                'titulo':'Titulo',
                'encabezado':'Encabezado',
                'texto':'Texto',
                'imagen':'Imagen',
                'categoria':'Categoria',
            }