# 06 - Escreva um programa onde o usuário digita uma frase e essa frase retorna sem nenhuma vogal.

frase_semVogal = input('Digite uma frase: ').lower()
resultado = ''
for i in frase_semVogal:
    if not i in "aeiou":
        resultado += i
print(resultado)