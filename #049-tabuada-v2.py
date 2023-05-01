#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
n = int(input('Número para tabuada: '))

for i in range(1,11):
    print('{} x {:2} = {}'.format(n, i, n*i))
