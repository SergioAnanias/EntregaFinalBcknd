from django.db import models
from django.utils.translation import gettext_lazy as _
from .validators import ParticipantesManager

class Institucion(models.Model):
    institucion_desc=models.CharField(max_length=255)

class Estados(models.TextChoices):
    RESERVADO = 'Reservado', 
    COMPLETADA = 'Completado', 
    ANULADA = 'Anulado', 
    NO_ASISTE = 'No Asiste', 


class Participante(models.Model):

    id = models.CharField(max_length=255, primary_key=True)
    nombre = models.CharField(max_length=255)
    fecha_inscripcion = models.DateField()
    institucion = models.ForeignKey('Institucion', models.DO_NOTHING)
    hora=models.TimeField()
    estado = models.CharField(max_length=255, choices=Estados.choices, default=Estados.RESERVADO, blank=True, null=True)
    observacion = models.CharField(max_length=255)
    objects=ParticipantesManager()