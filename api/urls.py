from django.urls import path
from .views import CancionApi, CargarDatosApi
urlpatterns = [
    path('cancion', CancionApi.as_view()),
    path('cargar-datos', CargarDatosApi.as_view())
]
