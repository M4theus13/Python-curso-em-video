""" Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
à vista dinheiro/cheque: 10% de desconto
à vista no cartão: 5% de desconto
em até 2x no cartão: preço formal 
3x ou mais no cartão: 20% de juros"""
valor = float(input('Preço das compras: R$'))
print("""FORMAS DE PAGAMENTO
\n[1] à vista dinheiro/cheque
\n[2] à vista cartão
\n[3] 2x no cartão
\n[4] 3x ou mais no cartão
""")
opt = int(input('Qual é a opção? '))
if opt == 1:
    desconto = valor * 10 / 100
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, valor - desconto))
elif opt == 2:
    desconto = valor * 5 / 100
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, valor - desconto))
elif opt == 3:
    parcela = valor / 2
    print('Sua compra será parcelada em 2x de {:.2f} SEM JUROS'.format(parcela))
    print('Sua compra vai custar R${:.2f} no final.'.format(valor))
elif opt == 4:
    vezes = int(input('Quantas parcelas? '))
    valorJuros = valor + (valor * 20 / 100) 
    parcela = ( valorJuros/ vezes)
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(vezes, parcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, valorJuros))
