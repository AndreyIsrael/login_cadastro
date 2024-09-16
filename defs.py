import valida
import time
import os
import sys

def limpaTerminal():
    return os.system('cls' if os.name == 'nt' else 'clear')

def criaBarra():
    return print('-' * 32)



def menu():
    print('______ <<< \033[1;96m''Lojas Maneiras''\033[0;0m'' >>> ______')
    print('[''\033[1;36m''1''\033[0;0m''] Cadastrar Cliente')
    print('[''\033[1;36m''2''\033[0;0m''] Mostrar Clientes')
    print('[''\033[1;36m''3''\033[0;0m''] Ver Compras:')
    print('[''\033[1;36m''0''\033[0;0m''] Sair')
    print('')
    x = input('\033[1;36m''Insira a opção: ''\033[0;0m')
    print('________________________________')
    return x
def cadastro():
    limpaTerminal()
    print('— < ''\033[1;92m''Cadastrar Usuário''\033[0;0m'' > —')

    nome = valida.nome_usuario()
    senha=valida.senha()
    with open('logins.txt', 'r') as lerlogins:
        for linha in lerlogins:
            linha = linha.strip()
            if not linha:
                continue
            valores = linha.split(' - ')
            if len(valores) != 2:
                continue
            try:
                nome_cadastrado = valores[0].split(':')[1].strip()
            except IndexError:
                continue
            if nome_cadastrado == "":
                continue
            if nome.lower() == nome_cadastrado.lower():
                limpaTerminal()
                criaBarra()
                print('\033[1;31m''Login já existente!''\033[0;0m')
                criaBarra()
                return
    lerlogins.close()
    limpaTerminal()
    criaBarra()
    print('\033[1;32m''Cliente Cadastrado com sucesso!''\033[0;0m')
    criaBarra()
    logins=open("logins.txt",'a')
    logins.write(f'nome: {nome} - senha: {senha}\n')
    logins.close()
    return



def compras():
    print('[''\033[1;36m''1''\033[0;0m''] Bolsa maneira:')
    print('[''\033[1;36m''2''\033[0;0m''] Colar maneiro:')
    print('[''\033[1;36m''3''\033[0;0m''] A coisa mais maneira da história:')
    print('[''\033[1;36m''0''\033[0;0m''] Sair:')
    x = input('\033[1;36m''Qual produto você deseja?: ''\033[0;0m')

    compras = open('maiscomprados.txt', 'a')
    compras.write(f'{x}\n')
    compras.close()
    cont1=0
    cont2=0
    cont3=0
    with open('maiscomprados.txt', 'r') as lercompras:
        for linha in lercompras:
            linha = linha.strip()
            if not linha:
                continue
            try:
                numero = int(linha)
                if numero == 1:
                    cont1 += 1
                elif numero == 2:
                    cont2 += 1
                elif numero == 3:
                    cont3 += 1
            except ValueError:
                continue


    conts=[cont1,cont2,cont3]
    maiscomprados=(max(conts))
    materiasmaiscomprados=[]
    if cont1==maiscomprados:
        materiasmaiscomprados.append('Produto[1]')
    if cont2==maiscomprados:
        materiasmaiscomprados.append('Produto[2]')
    if cont3==maiscomprados:
        materiasmaiscomprados.append('Produto[3]')
    materiasmaiscomprados_string = ','.join(materiasmaiscomprados)

    print('______ <<< \033[1;96m'f'Produto[1]={cont1} compras ''\033[0;0m'' >>> ______')
    print('______ <<< \033[1;96m'f'Produto[2]={cont2} compras ''\033[0;0m'' >>> ______')
    print('______ <<< \033[1;96m'f'Produto[3]={cont3} compras ''\033[0;0m'' >>> ______')
    print('______ <<< \033[1;96m'f'MAIS COMPRADOS={materiasmaiscomprados_string} ''\033[0;0m'' >>> ______')



def clientesCadastrados():
    with open('logins.txt','r') as lerlogins:
        for linha in lerlogins:
            print(linha.strip())



def login():
    cont_acesso = 0
    nome= valida.nome_usuario()
    senha= valida.senhalogin()
    with open('logins.txt','r') as lerlinhas:
        for linha in lerlinhas:
            linha=linha.strip()
            valores = linha.split(' - ')
            if not linha:
                continue
            if len(valores) != 2:
                continue
            try:
                nome_cadastrado = valores[0].split(':')[1].strip()
            except IndexError:
                continue
            if nome_cadastrado == "":
                continue
            if nome.lower() == nome_cadastrado.lower():
                limpaTerminal()
                criaBarra()
                print('Usuário encontrado!')
                criaBarra()
                cont_acesso += 1
            try:
                senhacadastrada = valores[1].split(':')[1].strip()
            except IndexError:
                    continue
            if senhacadastrada == "":
                continue
            if senha.lower() == senhacadastrada.lower():
                    cont_acesso += 1
                    limpaTerminal()
                    criaBarra()


            if cont_acesso == 2:
                cont_acesso = 0
                acesso_concedido()








def acesso_concedido():
    compras()

