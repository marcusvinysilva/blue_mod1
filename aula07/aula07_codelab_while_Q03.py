### 03 - Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# (C) Qual é o nome do produto mais barato. ###

total = mais1000 = mais_barato = unidade = 0
nome = ''
while True:
    produto = input('Produto: ').strip()
    preco = float(input('Preço do produto: R$ '))
    unidade += 1
    total += preco
    if preco > 1000:
        mais1000 += 1
    if unidade == 1:
        mais_barato = preco
        nome = produto
    else:
        if preco < mais_barato:
            mais_barato = preco
            nome = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N]: ').upper().strip()
    if continuar == 'N':
        break
print(f'O total da compra foi R${total:.2f}')
print(f'Quantidade de produtos que custam mais de R$ 1000.00: {mais1000}')
print(f'O produto mais barato é: {nome}')
