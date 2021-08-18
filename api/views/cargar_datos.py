from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import CancionSerializer
from ..helpers import load_data
from ..models import (
    Cancion, Artista, Instrumento, Label, BandasSimilares
)


class CargarDatosApi(APIView):
    def post(self, request):
        load_data(Cancion, Artista, Instrumento, Label, BandasSimilares)
        return Response(status=status.HTTP_200_OK)
