"""Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""
v1 = float(input('Primeiro valor: '))
v2 = float(input('Segundo valor: '))
opt = 0
while opt != 5:
    print("""
    [ 1 ] somar\n
    [ 2 ] multiplicar\n
    [ 3 ] maior\n
    [ 4 ] novos números\n
    [ 5 ] sair do programa""")
    opt = int(input('Qual sua opção?'))

    if opt == 1:
        print(v1 + v2)

    elif opt == 2:
        print(v1 * v2)

    elif opt == 3:
        if v1 > v2:
            print(v1)
        if v2 > v1:
            print(v2)

    elif opt == 4:
        v1 = float(input('Primeiro valor: '))
        v2 = float(input('Segundo valor: '))

    elif opt == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
print('Programa finalizado')