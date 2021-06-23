#01 - Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já esteja lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []

while True:
    num = int(input('\nDigite um valor: '))
    if num not in lista:
        lista.append(num)
    else:
        print('\nO valor já foi adicionado. Digite outro número!')
    continuar = input('\nDeseja adicionar outro número? [S/N]: ').upper()
    if continuar == 'N':
        break
print()
print(sorted(lista))