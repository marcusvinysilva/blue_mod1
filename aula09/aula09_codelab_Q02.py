#02 - Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista = []
lista_par = []
lista_impar = []

while True:
    num = int(input('\nDigite um valor: '))
    if num not in lista:
        lista.append(num)
        if (num % 2) == 0:
            lista_par.append(num)
        elif (num % 2) == 1:
            lista_impar.append(num)
    else:
        print('\nO valor já foi adicionado. Digite outro número!')
    continuar = input('\nDeseja adicionar outro número? [S/N]: ').upper()
    while continuar not in 'SN':
        continuar = input('\nDeseja adicionar outro número? [S/N]: ').upper()
    if continuar == 'N':
        break

print(f'\nLista principal:\n{sorted(lista)}')
print(f'\nLista de números pares:\n{sorted(lista_par)}')
print(f'\nLista de números ímpares:\n{sorted(lista_impar)}')