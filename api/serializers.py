from rest_framework import serializers
from .models import *


class CreatableSlugRelatedField(serializers.SlugRelatedField):
    def to_internal_value(self, data):
        try:
            return self.get_queryset().get_or_create(**{self.slug_field: data})[0]
        except ObjectDoesNotExist:
            self.fail('does_not_exist', slug_name=self.slug_field, value=smart_text(data))
        except (TypeError, ValueError):
            self.fail('invalid')

class ParticipanteSerializer(serializers.ModelSerializer):
    institucion = CreatableSlugRelatedField(
        slug_field='institucion_desc',
        queryset=Institucion.objects.all()
    )

    class Meta:
        model = Participante
        fields='__all__'
    
class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields='__all__'
