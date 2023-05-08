from rest_framework import serializers
from games.models import Categoria, Juego

class JuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juego
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    categoria = JuegoSerializer(many=True, read_only=True)

    class Meta:
        model = Categoria
        fields = ('id', 'nombre', 'imagen', 'background', 'descripcion', 'categoria')
