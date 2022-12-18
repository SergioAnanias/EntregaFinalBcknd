from django.db import models
import re
from datetime import datetime, date

class ParticipantesManager(models.Manager):
    def validator(self, postdata):
        errors={}

        if len(postdata["id"]) == 0:
            errors["id"] = "El campo rut se encuentra vacio"
            exists = super().get_queryset().filter(id=postdata["id"])        
        elif len(postdata["id"])>0:
            #Valida el rut
            RUT_REGEX=re.compile(r'^(\d{1,2})(\d{3})(\d{3})-(\w{1})$')
            if not re.match(RUT_REGEX, postdata["id"]):
                errors["rut"]="RUT no valido"
        if len(postdata["nombre"]) == 0:
            errors["nombre"] = "El campo nombre se encuentra vacio"
        if len(postdata["fecha_inscripcion"]) == 0 or len(postdata["fecha_inscripcion"]) < 10 or datetime.strptime(postdata["fecha_inscripcion"], "%Y-%m-%d") > datetime.now(): 
            errors["age"] = "Debe ingresar una fecha de nacimiento valida"
        if len(postdata['institucion'])==0:
            errors["institucion"] = "El campo institución se encuentra vacio"
        if len(postdata['observacion'])==0:
            errors["observacion"] = "El campo observación se encuentra vacio"
        if len(postdata['hora'])==0:
            errors["hora"] = "El campo hora se encuentra vacio"
        return errors
        