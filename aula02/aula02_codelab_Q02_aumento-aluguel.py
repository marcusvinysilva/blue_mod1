# Calculadora de aumento de aluguel
# Vamos construir um programa que irá calcular o aumento anual do seu aluguel.
# A sua calculadora vai receber o valor do aluguel e calcular o aumento baseado no IGPM de 31%. A calculadora deve apresentar o aluguel reajustado no formato R$ XXXX.XX.

valorIGPM = 31 / 100

valorAluguel = float(input('Qual o valor do seu aluguel?'))

print(f'O seu aluguel reajustado ficará no valor de {(valorAluguel + (valorAluguel * valorIGPM)):.2f} reais.')
