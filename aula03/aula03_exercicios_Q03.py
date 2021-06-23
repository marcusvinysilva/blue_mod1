# 03 – Faça um programa que solicite a altura e o peso do usuário, e calcule o seu IMC. Os dados entrados precisam ser corrigidos pelo programa (trocando “,” por “.” e eliminando espaços e letras extras).

altura = float(input('Informe a sua altura (em metros): ').replace(',','.'))
peso = float(input('Informe o seu peso (em KG): ').replace(',','.'))
imc = peso / (altura**2)
print()
print(f'O seu IMC é: {imc:.1f}')