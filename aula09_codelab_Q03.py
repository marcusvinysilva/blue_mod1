# Desafio: Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6  números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta

import random

jogos = []

quantidade_jogos = int(input('Quantos jogos você deseja? '))

for i in range(quantidade_jogos):
    count = 0 
    lista = [] 
    while True:
        num = random.randint(1,60)
        if num not in lista:
            lista.append(num)
            count += 1
            if count == 6:
                break
    lista.sort()
    jogos.append(lista)
    print(f'Jogo {i+1}: {jogos[i]}')

