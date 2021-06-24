# 3.Faça um Programa que leia 4 notas, mostre as notas e a média na tela
notas = []
for n in range(4):
	nota = float(input(f'Digite a {n+1}ª nota: '))
	notas.append(nota)
media = sum(notas)/4
print()
cont = 0
for i in notas:
	cont += 1
	print(f'{cont}ª nota: {i}')
print()
print(f'A média foi: {media}')