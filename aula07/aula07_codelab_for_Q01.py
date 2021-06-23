### 01 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos. ###

menor = 0
maior = 0

for i in range(1,6):
    peso = float(input(f'informe o peso da {i}ª pessoa (em KG): ').replace(',','.'))
    if i == 1:
        menor = peso
        maior = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso

print(f'O menor peso foi {menor} KG e o maior peso foi {maior} KG')