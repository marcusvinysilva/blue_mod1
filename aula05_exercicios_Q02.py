# 2 - Escreva um programa que pede a senha uma senha ao usuário, e só sai do loop quando digitarem
# corretamente a senha. A senha é “Blue123”
# 2b - Exiba quantas vezes o usuário errou a digitação

senha = "Blue123"
tentativa = input("Digite a senha: ")
contador = 0
while senha != tentativa:
    contador += 1
    print("Senha incorreta! Tente novamente!")
    tentativa = input("\nDigite a senha: ")

print("Senha correta!")

print(f'\nVocê errou a senha {contador} vezes')
