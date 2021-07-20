# 3- Faça um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.
import random
palavras = ["ABACATE", "ABACAXI", "ACEROLA", "GOIABA", "AMORA", "BANANA", "MORANGO", "CACAU", "CEREJA"]
palavra_sorteada = random.choice(palavras)
forca = []
for i in range(len(palavra_sorteada)):
    forca.append('_')
print(' '.join(forca))
print(f'A palavra tem {len(palavra_sorteada)} letras.')

tentativa = 6
while tentativa > 0 and forca.count('_') != 0:
    palpite = input('\nEscolha uma letra: ').upper()
    print()
    if palpite in palavra_sorteada:
        for letra in range(len(palavra_sorteada)):
            if palpite == palavra_sorteada[letra]:
                del forca[letra]
                forca.insert(letra,palpite)
        print(''.join(forca))
        print(f'A palavra tem {len(palavra_sorteada)} letras.')
    else:
        tentativa -= 1
        print(f'A palavra não tem essa letra. Você ainda tem {tentativa} tentativa(s).')
        print(''.join(forca))
        print(f'A palavra tem {len(palavra_sorteada)} letras.')

if forca.count('_') == 0:
    print(f'\n{palavra_sorteada}\nVOCÊ GANHOU!!!')
else:
    print(f'\nFORCA!!! Você perdeu! A palavra era {palavra_sorteada}')