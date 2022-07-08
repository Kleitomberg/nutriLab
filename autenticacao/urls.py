from unittest.mock import patch
from django.urls import path

from .views import *

urlpatterns = [
    path('cadastro/', cadastro, name="cadastro"),
    path('login/', logar, name="login"),
]