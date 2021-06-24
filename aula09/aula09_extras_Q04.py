# 4.Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as
lista = []
for i in range(10):
	letra = input('Digite uma letra: ')
	lista.append(letra)

cont = 0
lista_consoantes = []	
for l in lista:
	if l not in 'aeiouAEIOU':
		cont += 1
		lista_consoantes.append(l)
print()
print(f'As consoantes são: {lista_consoantes}')