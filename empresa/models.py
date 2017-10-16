from django.db import models
from django.utils import timezone

class Post(models.Model):
    nombre_empresa = models.CharField(max_length=200)
    persona = models.CharField(max_length=200)
    fecha = models.DateTimeField(default=timezone.now)
    puntuacion = models.CharField(max_length=4)


    def __str__(self):
        return self.nombre_empresa
