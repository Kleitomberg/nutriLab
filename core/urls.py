
from django.urls import path

from .views import *

urlpatterns = [

    path('pacientes/', pacientes, name="pacientes"),
    path('pacientes_dados_listar/', pacientes_dados_list, name='dados_paciente_list'),
    path('paciente_dados/<int:pk>', paciente_dados, name='paciente_dados'),
    path('grafico_peso/<int:id>/', grafico_peso, name="grafico_peso"),
]