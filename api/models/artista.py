from django.db import models
from .cancion import Cancion


class Artista(models.Model):
    nombre = models.CharField(max_length=255)
    cancion = models.ForeignKey(Cancion, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Artista'
        verbose_name_plural = 'Artistas'

    def __str__(self):
        return f'{self.id} - {self.nombre}'
