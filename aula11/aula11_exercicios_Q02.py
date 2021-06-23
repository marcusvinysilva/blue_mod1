### 2- Crie um programa, utilizando dicionário, que simule a baixa de estoque das vendas de um supermercado. Não esqueça de fazer as seguintes validações:​

# Produto Indisponível​
# Produto Inválido​
# Quantidade solicitada não disponível ​

# O programa deverá mostrar para o cliente a quantidade de itens comprados e o total.

estoque = {'batata':15, 'pão':10, 'café': 5}

while True:
    produto = input('O que você deseja comprar hoje? [digite 0 para finalizar] ').replace('pao', 'pão').replace('cafe','café')
    if produto == '0':
        break
    quantidade = int(input(f'Qual a quantidade de {produto}: '))
    if produto in estoque.keys(): 
        if estoque[produto] >= quantidade:
            print('O produto foi adicionado ao carrinho')
            estoque[produto] -= quantidade
        elif estoque[produto] == 0:
            print('Produto Indisponível')
        elif estoque[produto] < quantidade:
            print('Quantidade solicitada não disponível') 
    elif produto not in estoque.keys():
        print('Produto Inválido')

print(estoque)