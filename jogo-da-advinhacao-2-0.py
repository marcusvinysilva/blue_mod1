# Crie um jogo onde o computador vai “pensar” em um número entre 0 e 10. O jogador vai tentar
# adivinhar qual número foi escolhido até acertar, mostrando no final quantos palpites foram
# necessários para vencer.

import random
valor_aleatorio = random.randint(0,10)
print('O programa gerou um número entre 0 e 10. Advinhe qual é esse número.')
acertou = False
tentativas = 0
while not acertou:
    res1 = int(input("\nQual é o seu palpite? "))
    tentativas += 1
    if valor_aleatorio == res1:
        acertou = True
    else:
        print('\nVocê errou. Tente novamente!')

print(f'\nVocê acertou com {tentativas} tentativas.')
