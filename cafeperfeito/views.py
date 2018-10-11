# import OpenSSL
from django.shortcuts import render, redirect
from django.contrib import messages

from pkcs11 import lib, TokenNotRecognised, TokenNotPresent, Attribute, ObjectClass

# from cafeperfeito.models import Tabcolaborador

tokenLabel = ''


def index(request):
    return render(request, 'cafeperfeito/index.html')


def login(request):
    return render(request, 'cafeperfeito/login.html')
    # if request.method == 'POST':
    #     nusuario = request.POST.get('usuarios')
    #     senha = request.POST.get('senha')
    #
    #     usuario = Tabcolaborador.autentica_login('', nusuario, senha)
    #     if usuario.first() is not None:
    #         context = {
    #             'usuario_list': usuario,
    #         }
    #         return render(request, 'cafeperfeito/index.html', context)
    #
    #     else:
    #         messages.error(request, 'Error wrong username/password')
    # usuarios = Tabcolaborador.objects.all()
    # return render(request, 'cafeperfeito/login.html', {'usuarios': usuarios})
