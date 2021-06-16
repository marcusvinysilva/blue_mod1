### 04 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o. Mostre também quantos valores pares foram digitados. ###
soma = 0
num_par = 0
for i in range(1, 7):
    numero = int(input(f'Digite o {i}º número: '))
    if (numero % 2) == 0:
        soma += numero
        num_par += 1

print(f'\nA soma dos números pares é: {soma}')
print(f'\nForam digitado(s) {num_par} número(s) par(es)')