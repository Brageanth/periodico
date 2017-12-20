from django import forms
from .models import Noticia
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
            
class RegistroFrom(UserCreationForm):
    
    class Meta:
        model = User
        fields = [ 
                'username',
                'first_name',
                'last_name',
                'email',
            ]
        labels = {
                'username': 'Nombre de Usuario',
                'first_name': 'Nombre',
                'last_name': 'Apellidos',
                'email': 'Correo electronico',
            }
        widgets = {
                'username':forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}),
            }