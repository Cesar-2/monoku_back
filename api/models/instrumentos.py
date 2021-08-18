from django.db import models
from .cancion import Cancion


class Instrumento(models.Model):
    nombre = models.CharField(max_length=255)
    cancion = models.ForeignKey(Cancion, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Instrumento'
        verbose_name_plural = 'Instrumentos'

    def __str__(self):
        return f'{self.id} - {self.nombre}'
