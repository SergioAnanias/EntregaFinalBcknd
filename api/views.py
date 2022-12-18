from rest_framework import viewsets,permissions, status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import QueryDict
from .serializers import ParticipanteSerializer, InstitucionSerializer
from .models import Participante,Institucion


class Participantes(APIView):
    """
        Creación de participantes y obtención de todos los participantes
    {
        "id": "18875885-3",
        "institucion": "La pola1r",
        "nombre": "djlask",
        "fecha_inscripcion": "2020-10-10",
        "hora": "15:00:00",
        "observacion": "jdlkasjd"
    }
    """
    def get(self, request, format=None):
        participantes= Participante.objects.all()
        serial = ParticipanteSerializer(participantes, many=True)
        return Response(serial.data)
        
    def post(self, request):
        errors = Participante.objects.validator(request.POST)
        if len(errors) > 0:
            errors = {'errors':errors}
            return Response(errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        create = ParticipanteSerializer(data=request.data)
        if create.is_valid():
            create.save()
            return Response(create.data,status=status.HTTP_201_CREATED)
        return Response(create.errors, status=status.HTTP_400_BAD_REQUEST)

class DetalleParticipantes(APIView):
    """
        Funciones relacionadas a participantes individuales
    """
    def get_object(self, pk):
        return Participante.objects.get(id=pk)
    def get(self,request,pk):
        participante = self.get_object(pk)
        serialize=ParticipanteSerializer(participante)
        return Response(serialize.data)
    def put(self,request,pk):
        participante = self.get_object(pk)
        update = ParticipanteSerializer(participante, data=request.data)
        if update.is_valid():
            update.save()
            return Response(update.data,status=status.HTTP_202_ACCEPTED)
        return Response(update.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        participante = self.get_object(pk)
        participante.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def instituciones(request):
    instituciones=Institucion.objects.all()
    serial = InstitucionSerializer(instituciones, many=True)
    return Response(serial.data)

@api_view(['GET'])
def institucion_by_id(request,pk):
    institucion = Institucion.objects.get(id=pk)
    serial= InstitucionSerializer(institucion)
    return JsonResponse(serial.data)
    