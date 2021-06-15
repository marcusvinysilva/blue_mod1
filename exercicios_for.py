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


# 02 - Desenvolva um código que pergunte um número n para o usuário e exiba todos seus divisores

n = int(input('Digite um número: '))

print(f'\nOs divisores de {n} são:')

for i in range(1, n):
    if n % i == 0:
        print(i)


# 03 - Faça um script que o usuário escolha um número de início, um número de fim, e um número de passo.
# O programa deve printar todos os números do intervalo entre início e fim, "pulando" de acordo com o intervalo passado.

inicio = int(input('Número de ínicio: '))
fim = int(input('Número de fim: '))
passo = int(input('Quanto será o intervalo de pulo? '))

for i in range(inicio, fim+1, passo):
    print(i)


# 04 - Desenvolva um código em que o usuário vai entrar vários números e no final vai apresentar a soma deles (o usuário vai dizer quantos números serão informados antes de começar)

quantidade_valores = int(input('Quantos valores serão usados na soma? '))
soma = 0
for i in range(1, quantidade_valores+1):
    valor = int(input(f'Qual o {i}º valor? '))
    soma += valor
print(f'A soma de todos os valores é {soma}')


# 05 - Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
for i in range(10, -1, -1):
    print(i)
    sleep(1)
print('EXPLOSÃO DE FOGOS!!!')

# 06 - Escreva um programa onde o usuário digita uma frase e essa frase retorna sem nenhuma vogal.

frase_semVogal = input('Digite uma frase: ').lower()
resultado = ''
for i in frase_semVogal:
    if not i in "aeiou":
        resultado += i
print(resultado)