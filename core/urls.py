
from django.urls import path

from .views import *

urlpatterns = [

    path('pacientes/', pacientes, name="pacientes"),
    path('pacientes_dados_listar/', pacientes_dados_list, name='dados_paciente_list'),
    path('paciente_dados/<int:pk>', paciente_dados, name='paciente_dados'),
    path('plano_alimentar_listar/', plano_alimentar_listar, name="plano_alimentar_listar"),
    path('plano_alimentar/<int:id>/', plano_alimentar, name="plano_alimentar"),
    path('refeicao/<int:id_paciente>/',refeicao, name="refeicao"),
    path('opcao/<str:id_paciente>/', opcao, name="opcao"),
    path('grafico_peso/<int:id>/', grafico_peso, name="grafico_peso"),
    path('export_refeicoes/', export_refeicoes, name="export_refeicoes"),
]