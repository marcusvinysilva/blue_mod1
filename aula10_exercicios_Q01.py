# 1 - Crie uma lista composta que recebe 5 nomes e 5 idades de clientes, utilizando o for e o if,
# verifique quais clientes são maiores de idade e quais são menores de idade e mostre na tela
# a seguinte frase para cada um deles: 'Fulano é maior de idade' ou 'Fulana é menor de idade'
# e também quantos são maiores e quantos são menores de idade.

lista_geral = []
count_maior = 0
count_menor = 0

for i in range(5):
    while len(lista_geral) < 5:
        lista_individual = []
        nome = input('\nDigite o seu nome: ')
        idade = int(input('Digite a sua idade: '))
        lista_individual.append(nome)
        lista_individual.append(idade)
        if idade >= 18:
            lista_individual.append('maior de idade')
            count_maior += 1
        else:
            lista_individual.append('menor de idade')
            count_menor += 1
        lista_geral.append(lista_individual)
print()
for p in lista_geral:
    print(f'Nome: {p[0]}, Idade: {p[1]} anos ({p[2]})')
print()
print(f'{count_maior} pessoas são maiores de idade')
print(f'{count_menor} pessoas são menores de idade')