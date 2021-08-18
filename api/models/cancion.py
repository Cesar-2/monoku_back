from django.db import models


class Cancion(models.Model):
    fecha = models.DateTimeField()
    id_externo = models.IntegerField()
    nombre = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    banda = models.CharField(max_length=255)
    duracion = models.CharField(max_length=255)
    genero = models.CharField(max_length=255)
    subgenero = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Cancion'
        verbose_name_plural = 'Canciones'

    def __str__(self):
        return f'{self.id} - {self.nombre}'
