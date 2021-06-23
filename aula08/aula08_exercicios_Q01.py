# 1- Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
# a) tamanho da lista.
# b) maior valor da lista.
# c) menor valor da lista.
# d) soma de todos os elementos da lista.
# e) lista em ordem crescente.
# f) lista em ordem decrescente.

L = [5, 7, 2, 9, 4, 1, 3]
print(f'O tamanho da lista é: {len(L)}')
print(f'O maior valor da lista é: {max(L)}')
print(f'O menor valor da lista é: {min(L)}')
print(f'A soma de todos os elementos da lista é: {sum(L)}')
print(f'A lista em ordem crescente: {sorted(L)}')
print(f'A lista em ordem decrescente: {sorted(L, reverse=True)}')