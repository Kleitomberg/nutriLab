
from django.urls import path

from .views import *

urlpatterns = [

    path('pacientes/', pacientes, name="pacientes"),
]