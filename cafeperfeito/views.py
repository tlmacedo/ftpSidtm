# -*- coding: utf-8 -*-
# import OpenSSL
from django.shortcuts import render, redirect
from django.contrib import messages

from pkcs11 import lib, TokenNotRecognised, TokenNotPresent, Attribute, ObjectClass

from cafeperfeito.models import Tabcolaborador

tokenLabel = ''


def index(request):
    return render(request, 'cafeperfeito/index.html')


def certificado(request):
    # if request.user.is_authenticated():
    #     return redirect('admin_page')

    if request.method == 'POST':
        nusuario = request.POST.get('usuarios')
        senha = request.POST.get('senha')

        usuario = Tabcolaborador.autentica_login('', nusuario, senha)
        if usuario.first() is not None:
            context = {
                'usuario_list': usuario,
            }
            return render(request, 'cafeperfeito/index.html', context)

        else:
            messages.error(request, 'Error wrong username/password')

    meuToken = token()
    session = meuToken.open('user_pin=4879')
    certificados = []
    subjects = []
    for certificado in session.get_objects({Attribute.CLASS: ObjectClass.CERTIFICATE}):
        certificados.append(certificado)
        # cert = OpenSSL.crypto.load_certificate(
        #     OpenSSL.crypto.FILETYPE_ASN1,
        #     certificado[Attribute.VALUE],
        # )
        # subjects.append(cert.get_subject().CN)
        # # print("meu certificado:", subjects)
        # certificados.append(cert)
    session.close
    # print("certificados type:", type(certificados))
    # print("minha lista certificados:", certificados[0])
    return render(request, 'cafeperfeito/teste.html',
                  {'meuToken': meuToken, 'certificados': certificados})
    # return render(request, 'cafeperfeito/certificado.html')


def login(request):
    # if request.user.is_authenticated():
    #     return redirect('admin_page')

    if request.method == 'POST':
        nusuario = request.POST.get('usuarios')
        senha = request.POST.get('senha')

        usuario = Tabcolaborador.autentica_login('',nusuario)
        if usuario.first() is not None:
            context = {
                'usuario_list': usuario,
            }
            return render(request, 'cafeperfeito/index.html', context)

        else:
            messages.error(request, 'Error wrong username/password')
    usuarios = Tabcolaborador.objects.all()
    return render(request, 'cafeperfeito/login.html', {'usuarios': usuarios})


def token():
    lib_token = lib('/usr/local/lib/libeTPKcs11.dylib')  # TokenSafeNet5100
    for slot in lib_token.get_slots(True):
        try:
            token = slot.get_token()
            return token
        except TokenNotPresent:
            print('Erro: TokenNotPresent!')
            return None
        except TokenNotRecognised:
            print('Erro: TokenNotRecognised!')
            return None
        print('ainda está no loop? será')
