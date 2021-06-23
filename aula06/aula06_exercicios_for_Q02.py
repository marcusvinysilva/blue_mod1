# 02 - Desenvolva um código que pergunte um número n para o usuário e exiba todos seus divisores

n = int(input('Digite um número: '))

print(f'\nOs divisores de {n} são:')

for i in range(1, n):
    if n % i == 0:
        print(i)