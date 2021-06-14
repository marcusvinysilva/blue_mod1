valorIGPM = 31 / 100

valorAluguel = float(input('Qual o valor do seu aluguel?'))

print(f'O seu aluguel reajustado ficará no valor de {(valorAluguel + (valorAluguel * valorIGPM)):.2f} reais.')
