#Escreva um programa que leia um valor em metros e exiba convertido em centimetros e milímetros
metros = int(input('Metro:'))

cm = metros*100
mm = metros*1000

print('Metros para Centimetros: {}cm'.format(cm))
print('Metros para Milímetros: {}mm'.format(mm))