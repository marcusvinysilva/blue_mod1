# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
lista = []
for i in range(10):
    num = int(input('Digite um número: '))
    lista.append(num)
print()
print(sorted(lista, reverse=True))