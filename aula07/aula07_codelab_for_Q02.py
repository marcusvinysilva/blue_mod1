### 02 - Crie um programa que pergunte ao usuário um número inteiro e faça a tabuada desse número. ###

res1 = int(input('Digite um número para ver a sua tabuada: '))

for i in range(1, 11):
    print(f'{res1} x {i} = {(res1 * i)}')