from django import forms
from .models import Noticia

class Noticia_Form(forms.ModelForm):
    
    class Meta:
        model=Noticia
        fields = [
                'texto',
                'titulo',
                'encabezado',
                'imagen',
                'categoria',
            ]
        
        # Este es el arreglo con las etiquetas para cada uno de los campos que
        # usaremos
        labels = {
                'texto':'',
                'titulo':'',
                'encabezado':'',
                'imagen':'Imagen',
                'categoria':'',
            }
        
        widgets = {
                'texto' : forms.Textarea(attrs={'placeholder': 'TEXTO'}),
                'titulo' : forms.TextInput(attrs={'placeholder': 'TITULO'}),
                'encabezado' : forms.TextInput(attrs={'placeholder': 'Encabezado'}),
            }