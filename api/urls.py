from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers
from api import views

router = routers.DefaultRouter()




urlpatterns = [
    path('api/participantes/', views.Participantes.as_view()),
    path('api/participantes/<str:pk>', views.DetalleParticipantes.as_view()),
    path('api/instituciones/<int:pk>', views.institucion_by_id),
    path('api/instituciones/', views.instituciones)
]