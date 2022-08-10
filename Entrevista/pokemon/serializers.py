from rest_framework import serializers
from .models import Tipo, Personaje

class TipoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tipo
        fields = '__all__'


class PersonajeListSerializer(serializers.ModelSerializer):

    tipo = TipoListSerializer(read_only=True)

    class Meta:
        model = Personaje
        fields = '__all__'