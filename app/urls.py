from django.urls import path, include
from app import views






urlpatterns = [
    path('',views.index),
    path('delete/<str:id>', views.borrar),
    path('create',views.create),
    path('editar/<str:id>',views.editar),
    path('edit',views.edit)
]