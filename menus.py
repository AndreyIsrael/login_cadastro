import main
senhaadm=(123)
def menuclient():
    main.menuclient()

def madm():
    senha= int(input('Senha:'))
    if senhaadm==senha:
        main.menuadm()

def switch_case(key):
    if key == 1:


        menuclient()


    elif key == 2:
        madm()

    else:
        print('Escolha inválida')
while True:
    print('______ <<< \033[1;96m''Lojas Maneiras[MENUS]''\033[0;0m'' >>> ______')
    print('[''\033[1;36m''1''\033[0;0m''] Menu do cliente')
    print('[''\033[1;36m''2''\033[0;0m''] Menu do adm ')
    print('[''\033[1;36m''0''\033[0;0m''] Sair ')
    key = int(input('Sua escolha:'))
    if key ==0:
        print("encerrando sistema...")
        break
    switch_case(key)

















