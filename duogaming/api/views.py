from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from games.models import Categoria, Juego
from .serializers import CategoriaSerializer, JuegoSerializer

class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class JuegoList(generics.ListCreateAPIView):
    queryset = Juego.objects.all()
    serializer_class = JuegoSerializer
