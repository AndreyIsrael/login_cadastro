import valida
import defs

defs.limpaTerminal()

def menuadm():
    while True:
        escolha = defs.menu()

        if escolha == '1':
            defs.cadastro()
        elif escolha == '2':
            defs.clientesCadastrados()
        elif escolha == '3':
            defs.compras()
        elif escolha == '0':
            print('\033[1;36m''Encerrando...''\033[0;0m')
            break
        else:
            defs.limpaTerminal()
            defs.criaBarra()
            print('\033[1;31m''Insira uma opção válida!''\033[0;0m')
            defs.criaBarra()

def menuclient():
    while True:
        print('______ <<< \033[1;96m''Lojas Maneiras''\033[0;0m'' >>> ______')
        print('[''\033[1;36m''1''\033[0;0m''] Cadastrar Cliente')
        print('[''\033[1;36m''2''\033[0;0m''] Login')
        print('[''\033[1;36m''0''\033[0;0m''] Sair')
        print('')
        print('________________________________')
        escolha = (input('Digite sua escolha:'))

        if escolha == '1':
            defs.cadastro()
        elif escolha == '2':
            defs.login()
        elif escolha == '0':
            print('\033[1;36m''Obrigado pela preferencia!''\033[0;0m')
            break
        else:
            defs.limpaTerminal()
            defs.criaBarra()
            print('\033[1;31m''Insira uma opção válida!''\033[0;0m')
            defs.criaBarra()


