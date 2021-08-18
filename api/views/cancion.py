from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import CancionSerializer


class CancionApi(APIView):
    def post(self, request):
        def validar_fecha(fecha): return datetime.strptime(fecha, '%Y-%m-%d')
        validator = Validator({
            'fecha': {
                'required': True, 'type': 'string', 'coerce': validar_fecha
            },
            'id_externo': {'required': True, 'type': 'integer'},
            'nombre': {'required': True, 'type': 'string'},
            'album': {'required': True, 'type': 'string'},
            'banda': {'required': True, 'type': 'string'},
            'duracion': {'required': True, 'type': 'string'},
            'genero': {'required': True, 'type': 'string'},
            'subgenero': {'required': True, 'type': 'string'}
        })
        if not validator.validate(request.data):
            return Response({
                'codigo': 'Formato invalido',
                'data': validator.errors
            },
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = CancionSerializer()

        cancion = serializer.create(request.data)

        return Response({
            'pk': cancion
        }, status=status.HTTP_201_CREATED)

    def get(self, request):
        validator = Validator({
            'banda_similar': {'required': False, 'type': 'string'},
            'genero': {'required': False, 'type': 'string'},
            'subgenero': {'required': False, 'type': 'string'}
        })
        if not validator.validate(request.GET):
            return Response({
                'codigo': 'Formato invalido',
                'data': validator.errors
            },
                status=status.HTTP_400_BAD_REQUEST
            )

        filters = {}

        if request.GET.get('banda_similar'):
            filters['banda_similar__icontains'] = request.GET['banda_similar']

        if request.GET.get('genero'):
            filters['genero__icontains'] = request.GET['genero']

        if request.GET.get('subgenero'):
            filters['subgenero__icontains'] = request.GET['subgenero']

        serializer = CancionSerializer()

        canciones = serializer.get_canciones(filters)

        return Response({
            CancionSerializer(canciones, many=True).data
        }, status=status.HTTP_200_OK)
