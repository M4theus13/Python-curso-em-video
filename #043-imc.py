"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e 
mostre seu status, de acordo com a tabela abaixo:
IMC abaixo de 18,5: Abaixo do Peso
Entre 18,5 e 25: Peso Ideal
25 até 30: Sobrepeso
30 até 40: Obesidade
Acima de 40: Obesidade Mórbida"""
peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura**2)

print('Seu IMC é de {:.1f} você está na faixa de'.format(imc), end=' ')
if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc == 18.5 or imc < 25:
    print('PESO IDEAL')
elif imc == 25 or imc < 30:
    print('SOBREPESO')
elif imc == 30 or imc < 40:
    print('OBESIDADE')
elif imc >= 40:
    print('OBESIDADE MÓRBIDA')
else:
    print('Valor não reconhecido')