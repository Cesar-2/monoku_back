import copy
from rest_framework import serializers
from ..models import (
    Cancion, Artista, Instrumento, Label, BandasSimilares
)


class CancionSerializer(serializers.ModelSerializer):
    artista = serializers.SerializerMethodField()
    bandas_similares = serializers.SerializerMethodField()
    instrumentos = serializers.SerializerMethodField()
    label = serializers.SerializerMethodField()

    class Meta:
        model = Cancion
        fields = [
            'id', 'fecha',  'id_externo', 'nombre', 'album', 'banda',
            'duracion', 'genero', 'subgenero', 'artista', 'bandas_similares',
            'instrumentos', 'label'
        ]

    def get_artista(self, obj):
        return Artista.objects.filter(cancion=obj.id)

    def get_bandas_similares(self, obj):
        return BandasSimilares.objects.filter(cancion=obj.id)

    def get_intrumentos(self, obj):
        return Instrumento.objects.filter(cancion=obj.id)

    def get_label(self, obj):
        return Label.objects.filter(cancion=obj.id)

    def create(self, data):
        return Cancion.objects.create(**data).id

    def get_canciones(self, filters):
        aux = copy.deepcopy()
        aux.pop('bandas_similares__icontains')
        if 'bandas_similares__icontains' in filters:
            aux['id'] = BandasSimilares.objects.filter(
                nombre=filters["bandas_similares__icontains"]).first()
        return Cancion.objects.filter(**aux)
