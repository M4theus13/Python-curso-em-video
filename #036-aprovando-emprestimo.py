""" Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode 
exceder 30% do salário ou então o empréstimo será negado."""
valorCasa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
parcelas = valorCasa // (anos * 12)
porcentagemSalario = salario * 30 / 100
if porcentagemSalario > parcelas:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f} \nEmprestimo APROVADO!'.format(valorCasa, anos, parcelas))
else:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f} \nEmprestimo NEGADO!'.format(valorCasa, anos, parcelas))
    