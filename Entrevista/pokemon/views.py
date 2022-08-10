from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Tipo, Personaje
from .serializers import TipoListSerializer, PersonajeListSerializer

# Create your views here.
class RegisterTipoView(APIView):

    def post(self, request):
        data = request.data
        tipo_serializer = TipoListSerializer(data=data)
        tipo_serializer.is_valid()
        tipo_serializer.save()
        return Response({'Tipo de personaje creado exitosamente'}, status = status.HTTP_200_OK)

class RegisterTipoDetailView(APIView):

    def get(self, request, pk=None):
        tipo = Tipo.objects.get(id = pk)
        tipo_serializer = TipoListSerializer(tipo)
        return Response({'mensaje':'lista de tipos de personajes','data':tipo_serializer.data}, status = status.HTTP_200_OK)

    def put(self, request, pk=None):
        tipo = Tipo.objects.get(id = pk)
        tipo_serializer = TipoListSerializer(tipo, data=request.data, partial=True)
        tipo_serializer.is_valid()
        tipo_serializer.save()
        return Response({'Tipo de personaje modificado exitosamente'}, status = status.HTTP_200_OK)


class RegisterPersonajeView(APIView):

    def get(self, request):
        personajes = Personaje.objects.all()
        personaje_serializer = PersonajeListSerializer(personajes, many=True)
        return Response({'mensaje':'lista de personajes','data':personaje_serializer.data}, status = status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        personaje_serializer = PersonajeListSerializer(data=data)
        personaje_serializer.is_valid()
        personaje_serializer.save()
        return Response({'Personaje creado exitosamente'}, status = status.HTTP_200_OK)
        
class RegisterPersonajeDetailView(APIView):

    def get(self, request, pk=None):
        personaje = Personaje.objects.get(id = pk)
        personaje_serializer = PersonajeListSerializer(personaje)
        return Response({'mensaje':'lista de personajes','data':personaje_serializer.data}, status = status.HTTP_200_OK)