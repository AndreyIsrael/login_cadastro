import time


def nome_usuario():
    while True:
        nome = input('Nome completo:').strip()
        if nome == '':
            print('Erro: Entrada vazia.')
            continue
        temp = ''.join(nome.split())
        for i in temp:
            if i.isdigit():
                print('Digite um nome válido.')
                break
        else:
            return nome

def senha():
    while True:
        digitesenha= input('Senha:')
        if digitesenha=='':
            print('Erro: Entrada vazia.')
            continue
        tem_maiuscula = False
        tem_minuscula = False
        tem_numero = False
        tem_caractere_especial = False
        caracteres_especiais = "!@#$%^&*()-_=+[]{}|;:\,.<>?/"
        for char in digitesenha:
            if char.isupper():
                tem_maiuscula= True
            elif char.islower():
                tem_minuscula= True
            elif char.isdigit():
                tem_numero=True
            elif char in caracteres_especiais:
                tem_caractere_especial= True
        if tem_maiuscula and tem_minuscula and tem_numero and tem_caractere_especial:
            while True:
                digitesenha2= input('Digite novamente para confirmar a sua senha:')
                if digitesenha2==digitesenha:
                    print('Senha confirmada!')
                    return digitesenha
                else:
                    print('Erro: Senhas diferentes.')
                    break
        else:
            print('Erro: Digite sua senha com pelo menos 1: caractere especial; número; letra maiúscula e minúscula.')
            continue

def senhalogin():
    while True:
        digitesenha= input('Senha:')
        if digitesenha=='':
            print('Erro: Entrada vazia.')
            continue
        tem_maiuscula = False
        tem_minuscula = False
        tem_numero = False
        tem_caractere_especial = False
        caracteres_especiais = "!@#$%^&*()-_=+[]{}|;:\,.<>?/"
        for char in digitesenha:
            if char.isupper():
                tem_maiuscula= True
            elif char.islower():
                tem_minuscula= True
            elif char.isdigit():
                tem_numero=True
            elif char in caracteres_especiais:
                tem_caractere_especial= True
        if tem_maiuscula and tem_minuscula and tem_numero and tem_caractere_especial:
            return digitesenha

        else:
            print('Erro: Digite sua senha com pelo menos 1: caractere especial; número; letra maiúscula e minúscula.')
            continue




