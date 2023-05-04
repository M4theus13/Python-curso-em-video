"""Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, organizando os dados em forma tabular."""
listagem = ('Lápis', 1.75,
            'Borracha',2,
            'Caderno',15.90,
            'Estojo',9.99,
            'Mochila',119.99,
            'Canetas',5.90,
            'Livro',49)
for item in range(0, len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:-<30}',end='')
    else:
        print(f'R${listagem[item]:>8.2f}')