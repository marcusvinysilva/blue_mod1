# 3. Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela. A média para aprovação é 7. Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é reprovado.

dic_media = {}

while True:
    lista = []
    nome = str(input('Digite o nome do aluno: ').title())
    media = float(input(f'Digite a média de {nome}: ').replace(',','.'))
    lista.append(media)
    if media >= 7:
        lista.append('Aprovado')
    elif media >= 5 and media <= 6.9:
        lista.append('Recuperação')
    elif media < 5:
        lista.append('Reprovado')
    dic_media[nome] = lista
    continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if continuar == 'N':
        break
print()
print(dic_media)
print()
for i in dic_media:
    print(f'Aluno(a): {i}\nMédia = {dic_media[i][0]}\nSituação: {dic_media[i][1]}')
    print()