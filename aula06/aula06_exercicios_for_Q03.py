# 03 - Faça um script que o usuário escolha um número de início, um número de fim, e um número de passo. O programa deve printar todos os números do intervalo entre início e fim, "pulando" de acordo com o intervalo passado.

inicio = int(input('Número de ínicio: '))
fim = int(input('Número de fim: '))
passo = int(input('Quanto será o intervalo de pulo? '))

for i in range(inicio, fim+1, passo):
    print(i)