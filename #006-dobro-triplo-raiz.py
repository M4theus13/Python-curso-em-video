#Inserir um valor, e calcular a raiz quadrada, o dobro e o triplo
n = int(input('Insira um número para calcular sua raiz, seu dobro e seu triplo: '))

raiz = n**(1/2)
dobro = n*2
triplo = n*3

print('A raiz do número é {:.2f} \nO dobro do número é {} \nO triplo do número é {}' .format(raiz, dobro, triplo))
