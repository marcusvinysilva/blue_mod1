### 2- Crie um programa, utilizando dicionário, que simule a baixa de estoque das vendas de um supermercado. Não esqueça de fazer as seguintes validações:​

# Produto Indisponível​
# Produto Inválido​
# Quantidade solicitada não disponível ​

# O programa deverá mostrar para o cliente a quantidade de itens comprados e o total.

estoque = {'batata':[15,1.25], 'pão':[10,1], 'café': [5,8]}
dic_produtosComprados = {}

while True:
    lista_produto = []
    total_preco = 0
    produto = input('O que você deseja comprar hoje? [digite 0 para finalizar] ').replace('pao', 'pão').replace('cafe','café')
    if produto == '0':
        break
    quantidade = int(input(f'Qual a quantidade de {produto}: '))
    if produto in estoque.keys(): 
        if estoque[produto][0] >= quantidade:
            print('O produto foi adicionado ao carrinho')
            estoque[produto][0] -= quantidade
            lista_produto.append(quantidade)
            total_preco += (estoque[produto][1] * quantidade)
            lista_produto.append(total_preco)
            dic_produtosComprados[produto] = lista_produto
        elif estoque[produto][0] == 0:
            print('Produto Indisponível')
        elif estoque[produto][0] < quantidade:
            print('Quantidade solicitada não disponível') 
    elif produto not in estoque.keys():
        print('Produto Inválido')
print()
total_compras = 0
for i in dic_produtosComprados:
     print(f'Você comprou {dic_produtosComprados[i][0]} unidades de {i} e custou R$ {dic_produtosComprados[i][1]:.2f}')
     total_compras += dic_produtosComprados[i][1]
print(f'O total de suas compras deu R$ {total_compras:.2f}')