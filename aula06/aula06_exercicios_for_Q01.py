# 01 - Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte quantas vezes aparece as vogais a,e,i,o,u

frase = input('Escreva uma frase: ').upper()

countA = countE = countI = countO = countU = 0

for i in frase:
    if i == 'A':
        countA += 1
    elif i == 'E':
        countE += 1
    elif i == 'I':
        countI += 1
    elif i == 'O':
        countO += 1
    elif i == 'U':
        countU += 1

print(f'vogal A: {countA}')
print(f'vogal E: {countE}')
print(f'vogal I: {countI}')
print(f'vogal O: {countO}')
print(f'vogal U: {countU}')