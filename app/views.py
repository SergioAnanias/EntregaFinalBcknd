from api.views import *
from api.models import Participante,Estados
from django.shortcuts import render,redirect
import json
import requests
from django.http import QueryDict
from django.contrib import messages

def index(request):
    participantes = Participantes().get(request)
    participantes = json.dumps(participantes.data)
    participantes=json.loads(participantes)
    context={
        'participantes':participantes
    }
    return render(request,'index.html',context)
def borrar(request,id):
    DetalleParticipantes().delete(request,id)
    return redirect("/")

def crear(request):
    return render(request, "create.html")

def editar(request,id):
    participante = DetalleParticipantes().get_object(id)
    participante = ParticipanteSerializer(participante)
    estados = Estados
    context = {
        'participante':participante.data,
        'estados':estados
    }
    return render(request, "edit.html",context)

def create(request):
    setattr(request, 'data', request.POST)
    response = Participantes().post(request)
    if(response.status_code==500):
        for k, v in response.data['errors'].items():
            messages.error(request, v)
        return redirect("/")
    return redirect("/")

def edit(request):
    setattr(request, 'data', request.POST)
    print(request.POST.get('id'))
    rut=request.POST.get('id')
    DetalleParticipantes().put(request, rut)
    return redirect("/")