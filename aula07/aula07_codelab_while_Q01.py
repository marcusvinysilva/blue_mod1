### 01 - Crie um programa que leia dois valores e mostre um menu na tela:
### [ 1 ] somar
### [ 2 ] multiplicar
### [ 3 ] maior
### [ 4 ] novos números
### [ 5 ] sair do programa
### Seu programa deverá realizar a operação solicitada em cada caso. (utilizar while sem break) ###

num1 = int(input('Digite o primeiro número: ').replace(',','.'))
num2 = int(input('Digite o segundo número: ').replace(',','.'))
opcao = int(input('\n[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\nEscolha uma opção: '))

while opcao != 5:
    if opcao == 1:
        print(f'\n{num1} + {num2} = {(num1 + num2)}')
        opcao = int(input('\n[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\nEscolha uma opção: '))
    elif opcao == 2:
            print(f'\n{num1} x {num2} = {(num1 * num2)}')
            opcao = int(input('\n[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\nEscolha uma opção: '))
    elif opcao == 3:
         if num1 > num2:
             print(f'\nO {num1} é maior que o {num2}')
         elif num2 > num1:
             print(f'\nO {num2} é maior que o {num1}')
         opcao = int(input('\n[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\nEscolha uma opção: '))
    elif opcao == 4:
        num1 = int(input('Digite o primeiro número: ').replace(',','.'))
        num2 = int(input('Digite o segundo número: ').replace(',','.'))
        opcao = int(input('\n[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\nEscolha uma opção: '))
    else:
        print('\nOpção inválida. Digite novamente!')
        opcao = int(input('\n[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\nEscolha uma opção: '))

print('\nVocê saiu do programa.')