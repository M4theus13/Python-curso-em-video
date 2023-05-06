num = list()
for i in range(0,5):
    add = int(input(f'Digite um número para a posição {i}:'))
    num.append(add)
print(f'Você digitou os valores {num}')
ord = num[:]
ord.sort()
print(f'O maior valor digitado foi {ord[-1]}')
print(f'O menor valor digitado foi {ord[0]}')