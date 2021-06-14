valorDolar = 5.04
valorEuro = 6.13
valorLibra = 7.13
valorDolarCanadense = 4.16
valorPesoArgentino = 0.053
valorPesoChileno = 0.0070

quantidadeReal = float(input('Qual valor você quer converter?'))

print(f'Com {quantidadeReal} reais, você terá {(quantidadeReal / valorDolar):.2f} doláres')
print(f'Com {quantidadeReal} reais, você terá {(quantidadeReal / valorEuro):.2f} euros')
print(f'Com {quantidadeReal} reais, você terá {(quantidadeReal / valorLibra):.2f} libras')
print(f'Com {quantidadeReal} reais, você terá {(quantidadeReal / valorDolarCanadense):.2f} doláres canadenses')
print(f'Com {quantidadeReal} reais, você terá {(quantidadeReal / valorPesoArgentino):.2f} pesos argentinos')
print(f'Com {quantidadeReal} reais, você terá {(quantidadeReal / valorPesoChileno):.2f} pesos chilenos')
