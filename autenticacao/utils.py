from asyncio.windows_events import NULL
import re
from django.contrib import messages
from django.contrib.messages import constants

def password_is_valid(request, senha, confirmar_senha):

    if len(senha) <= 0 or senha == NULL or  senha == None or senha =="":
        messages.add_message(request, constants.ERROR,
                        'O Campo Senha é obrigatorio!')
        return False
    if len(senha) < 6:
        messages.add_message(request, constants.ERROR,
                        'Sua senha deve conter 6 ou mais caractertes')
        return False
    if not senha == confirmar_senha:
        messages.add_message(request, constants.ERROR, 'As senhas não coincidem!')
        return False
    if not re.search('[A-Z]', senha):
        messages.add_message(request, constants.ERROR,
                            'Sua senha não contem letras maiúsculas')
        return False
    if not re.search('[a-z]', senha):
        messages.add_message(request, constants.ERROR,
                            'Sua senha não contem letras minúsculas')
        return False
    if not re.search('[1-9]', senha):
        messages.add_message(request, constants.ERROR, 'Sua senha não contém números')
        return False
    return True


def email_is_valid(request, email):

    if len(email) <= 0 or email == NULL or  email == None or email =="":
        messages.add_message(request, constants.ERROR,'O Campo Email é obrigatorio!')
        return False

    if "@" not in email or "." not in email:
        messages.add_message(request, constants.ERROR,'E-mail não é valido!')
        return False

    return True

def username_is_valid(request, username):

    if len(username) <= 0 or username == NULL or  username == None or username =="":
        messages.add_message(request, constants.ERROR,'O Campo username é obrigatorio!')
        return False
    if  re.search('[1-9]', username):
        messages.add_message(request, constants.ERROR, 'O Username não pode ter numeros')
        return False

    return True