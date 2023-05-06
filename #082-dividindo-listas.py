"""Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão 
conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
Ao final, mostre o conteúdo das três listas geradas."""
num = list()
impar = list()
par = list()
while True:
    add = int(input('Digite um valor: '))
    stop = input('deseja parar? s/n: ').upper()
    num.append(add)
    
    if add % 2 == 0:
        par.append(add)
    else:
        impar.append(add)

    if stop == 'S':
        break
print(f'A lista completa é {num}')
print(f'A lista de pares é {par}')
print(f'A lista de impar é {impar}')