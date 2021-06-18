### 02 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) Quantas pessoas têm mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres têm menos de 20 anos. ###

homens = maior18 = mulher20 = 0
while True:
    idade =  int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo =  str(input('Sexo: [M/F]: ')).upper().strip()[0]      
    if idade >= 18:
        maior18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1         
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resposta == 'N':
        break

print(f'\nTotal de pessoas com mais de 18 anos: {maior18}')
print(f'Total de homens cadastrados: {homens}')
print(f'Total de mulheres com menos de 20 anos: {mulher20}')