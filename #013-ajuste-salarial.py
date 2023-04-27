#Programa que faz reajuste salarial de uma pessoa, podendo ser reajuste positivo ou negativo, e mostra todas informações
salario = float(input('Insira o salario: '))
porcentagem = float(input('Insira a porcentagem de reajuste: '))

reajuste = porcentagem * salario / 100

novoSalario = salario + reajuste

print('O funcionário que ganhava R${}, com um reajuste de {}%, passa a receber R${}'.format(salario, porcentagem, novoSalario))
