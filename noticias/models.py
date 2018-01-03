from django.db import models
from django.utils import timezone
    
class Noticia(models.Model):
        autor = models.ForeignKey('auth.User')
        titulo = models.CharField(max_length=100)
        encabezado = texto = models.TextField(max_length=200)
        texto = models.TextField()
        imagen = models.ImageField(upload_to='imagenes')
        fecha_creacion = models.DateTimeField(
                    default=timezone.now)
        fecha_publicacion = models.DateTimeField(
                    blank=True, null=True)
        SELECCION = 'SC'
        DEPORTES = 'DTI'
        ENTRETENIMIENTO = 'ER'
        ORDEN = 'OPA'
        CHIBCHOMBIA = 'Ch'
        NEGOCIOS = 'NO'
        CATEGORIAS = (
            (SELECCION, 'Seleccione una categoria'),
            (DEPORTES, 'Deportes tropicales de invierno'),
            (ENTRETENIMIENTO, 'Entretenimiento para robots'),
            (ORDEN, 'Orden Publico Alterado'),
            (CHIBCHOMBIA, 'Chibchombia'),
            (NEGOCIOS, 'Negocios ociosos'),
        )
        categoria = models.CharField(
            max_length=3,
            choices=CATEGORIAS,
            default=SELECCION,
        )
        destacado = models.NullBooleanField()
        
        def publish(self):
                self.fecha_publicacion = timezone.now()
                self.save()
    
        def __str__(self):
                return self.titulo
        
        def __unicode__(self,):
            return str(self.imagen)
        
        def estaLoguado(self):
            try:
                self.autor
                return True
            except:
                return False