# 04 - Desenvolva um código em que o usuário vai entrar vários números e no final vai apresentar a soma deles (o usuário vai dizer quantos números serão informados antes de começar)

quantidade_valores = int(input('Quantos valores serão usados na soma? '))
soma = 0
for i in range(1, quantidade_valores+1):
    valor = int(input(f'Qual o {i}º valor? '))
    soma += valor
print(f'A soma de todos os valores é {soma}')