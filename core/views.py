
from datetime import datetime
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect as red

from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.contrib.messages import constants
from django.urls import reverse_lazy, reverse
from django.views.decorators.csrf import csrf_exempt

from .utils import *

# Create your views here.

@login_required(login_url='/auth/login/')
def pacientes(request):
    if request.method =="GET":

        pacientes = Pacientes.objects.filter(nutri=request.user)
        return render(request, 'pacientes.html', {'pacientes': pacientes})
        
    elif request.method == "POST":

        nome = request.POST.get('nome')
        sexo = request.POST.get('sexo')
        idade = request.POST.get('idade')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')

        if not paciente_is_valid(request,email, nome, idade, telefone, sexo):
             return redirect('/pacientes/')
        
        try:
            paciente = Pacientes(
                nome=nome,
                sexo=sexo,
                idade=idade,
                email=email,
                telefone=telefone,
                nutri=request.user
                )

            paciente.save()
            messages.add_message(request, constants.SUCCESS, 'Paciênte cadastrado com sucesso')
            return redirect('/pacientes/')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/pacientes/')

@login_required(login_url='/auth/login/')
def pacientes_dados_list(request):
    if request.method == "GET":
        pacientes = Pacientes.objects.filter(nutri=request.user)
        return render(request, 'dados_paciente_listar.html', {'pacientes': pacientes})

def paciente_dados(request, pk):
    paciente = get_object_or_404(Pacientes, pk=pk)
    dados_paciente = DadosPaciente.objects.filter(paciente=paciente)
    if not paciente.nutri == request.user:
        messages.add_message(request, constants.ERROR, 'Esse paciente não é seu')
        return redirect('/pacientes_dados_listar/')

    if request.method == "GET":
        return render(request, 'dados_paciente.html', {'paciente': paciente, 'dados_paciente':dados_paciente},)

    elif request.method == "POST":
        peso = request.POST.get('peso')
        altura = request.POST.get('altura')
        gordura = request.POST.get('gordura')
        musculo = request.POST.get('musculo')

        hdl = request.POST.get('hdl')
        ldl = request.POST.get('ldl')
        colesterol_total = request.POST.get('ctotal')
        trigliceridios = request.POST.get('trigliceridios')

        if not paciente_dados_is_valid(request, peso,altura,gordura,musculo,hdl,ldl,colesterol_total,trigliceridios):             
             return redirect('/paciente_dados/')

        try:
            dados_paciente = DadosPaciente(
                peso=peso,
                altura=altura,
                percentual_gordura=gordura,
                percentual_musculo=musculo,
                colesterol_hdl=hdl,
                colesterol_ldl=ldl,
                colesterol_total = colesterol_total,
                trigliceridios=trigliceridios,
                data=datetime.now(),
            )
            dados_paciente.paciente = paciente
            dados_paciente.save()
            messages.add_message(request, constants.SUCCESS, 'Dados cadastrados com sucesso')
            
            return red('paciente_dados', paciente.id)
           

        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/pacientes_dados_listar/')



@login_required(login_url='/auth/logar/')
@csrf_exempt
def grafico_peso(request, id):
    paciente = Pacientes.objects.get(id=id)
    dados = DadosPaciente.objects.filter(paciente=paciente).order_by("data")
    
    pesos = [dado.peso for dado in dados]
    labels = list(range(len(pesos)))
    data = {'peso': pesos,
            'labels': labels}
    return JsonResponse(data)