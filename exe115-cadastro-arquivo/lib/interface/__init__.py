def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\33[31mERRO: por favor, digite um número inteiro válido. \33[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número. \033[m')
            return 0
        else:
            return n

def linha(tam = 42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    i = 1
    for item in lista:
        print(f'\033[33m{i}\033[33m - \033[34m{item}\033[34m')
        i += 1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc
