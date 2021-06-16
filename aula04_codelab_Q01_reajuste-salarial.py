# Reajuste salarial
# As empresas @.com resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5%
# Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento."

reajusteCategoria1 = 20
reajusteCategoria2 = 15
reajusteCategoria3 = 10
reajusteCategoria4 = 5

salarioAtual = float(input('Quanto é o seu salário atual? R$').replace(',','.'))

if salarioAtual <= 280:
    reajuste = salarioAtual * (reajusteCategoria1 / 100)
    porcentagem = reajusteCategoria1
elif 280 < salarioAtual <= 700:
    reajuste = salarioAtual * (reajusteCategoria2 / 100)
    porcentagem = reajusteCategoria2
elif 700 < salarioAtual <= 1500:
    reajuste = salarioAtual * (reajusteCategoria3 / 100)
    porcentagem = reajusteCategoria3
else:
    reajuste = salarioAtual * (reajusteCategoria4 / 100)
    porcentagem = reajusteCategoria4

novoSalario = salarioAtual + reajuste

print(f'\nO seu salário atual é R${salarioAtual:.2f}')
print(f'O percentual de reajuste foi de {porcentagem}%')
print(f'O valor do aumento é R${reajuste:.2f}')
print(f'O seu novo salário será R${novoSalario:.2f}')
