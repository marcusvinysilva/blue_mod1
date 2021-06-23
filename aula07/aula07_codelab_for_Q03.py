### 03 - Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. ###

menor18 = 0
for i in range(1,8):
    ano_nascimento = int(input(f'informe o ano de nascimento da {i}ª pessoa: '))
    if ano_nascimento > 2004:
        menor18 += 1
print(f'{menor18} pessoas ainda não atingiram a maior idade.')