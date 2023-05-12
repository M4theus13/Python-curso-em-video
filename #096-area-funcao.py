""" Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular 
(largura e comprimento) e mostre a área do terreno."""
def area(a,b):
    result = a * b
    return result

l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
metro = area(l,c)
print(f'A area de um terreno {l} x {c} é de {metro}m².')
