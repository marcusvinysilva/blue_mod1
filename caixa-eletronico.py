# Caixa eletrônico
# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
# O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

valor_saque = int(input('Qual será o valor do saque? (saque mínimo: R$10) R$'))

notas100 = int(valor_saque/100)
valor_saque = valor_saque % 100

notas50 = int(valor_saque/50)
valor_saque = valor_saque % 50

notas10 = int(valor_saque/10)
valor_saque = valor_saque % 10

notas5 = int(valor_saque/5)
valor_saque = valor_saque % 5

notas1 = valor_saque

print(f'{notas100} notas de R$100')
print(f'{notas50} notas de R$50')
print(f'{notas10} notas de R$10')
print(f'{notas5} notas de R$5')
print(f'{notas1} notas de R$1')
