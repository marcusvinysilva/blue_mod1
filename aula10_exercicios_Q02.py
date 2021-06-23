# 2 - Faça um programa que leia nome e altura de várias pessoas, guardando tudo em uma lista,
# depois do dado inserido, pergunte ao usuário se ele quer continuar, se ele não quiser pare o
# programa. No final mostre:
# a) Quantas pessoas foram cadastradas
# b) Mostre a maior altura
# c) Mostre a menor altura

quant_pessoas = 0
altura_maior = 0
altura_menor = 0
lista_final = []

while True:
    lista = []
    nome = input('Digite o seu nome: ').title().strip()
    lista.append(nome)
    quant_pessoas += 1
    altura = float(input('Informe a sua altura (em metros): ').replace(',','.'))
    lista.append(altura)
    if quant_pessoas == 1: 
        altura_maior = altura
        altura_menor = altura
    else:
        if altura > altura_maior:
            altura_maior = altura
        if altura < altura_menor:
            altura_menor = altura
    lista_final.append(lista)
    continuar = input('Deseja continuar? [S/N] ').upper()
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N] ').upper()
    if continuar == 'N':
        break
print()
print(lista_final)
print()
print(f'Total de pessoas cadastradas: {quant_pessoas}')
print(f'A maior altura é: {altura_maior}')
print(f'A menor altura é: {altura_menor}')