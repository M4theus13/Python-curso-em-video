"""Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e 
outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial."""
def fatorial(fat, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param fat: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for i in range(fat, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f*= i
    return f


print(fatorial(5, True))