# 01 – Escreva um programa que deve receber o nome completo do usuário e retornar uma saudação com o nome no formato adequado (todas as primeiras letras em maiúsculas).

nome = input('Digite o seu nome completo ').title().strip()
print(f'Olá, {nome}!')