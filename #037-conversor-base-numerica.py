"""Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a 
base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal."""
num = int(input('Digite um número inteiro: '))
print("""Escolha uma das bases para conversão:
\n[1] converter para BINÁRIO
\n[2] converter para OCTAL
\n[3] converter para HEXADECIMAL""")
escolha = int(input('Sua opção: '))
if escolha == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)))
elif escolha == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)))
elif escolha == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)))
else:
    print('Opção inválida.')
