# Jogo da adivinhação

# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 10
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
valor_aleatorio = random.randint(0,10)
res1 = int(input("O programa gerou um número entre 0 e 10. Que número foi esse?\nResposta: "))

if valor_aleatorio == res1:
  print('\nVocê venceu!')
else:
  print('\nVocê perdeu!')
  print(f'\nO número foi {valor_aleatorio}')
