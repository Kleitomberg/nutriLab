from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Pacientes)
admin.site.register(DadosPaciente)
admin.site.register(Refeicao)
admin.site.register(Opcao)