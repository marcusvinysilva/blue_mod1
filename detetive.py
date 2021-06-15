# crie um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# • "Você telefonou para a vítima?"
# • " Você esteve no local do crime?"
# • " Você mora perto da vítima?"
# • " Você devia para a vítima?"
# • " Você já trabalhou com a vítima?"
# O programa deve, no final, emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a:
# • 2 questões ela deve ser classificada como "Suspeita",
# • Entre 3 e 4 como "Cúmplice"
# • 5 como "Assassino".
# • Caso contrário, ele será classificado como "Inocente".

resposta1 = int(input("Você telefonou para a vítima?\nDigite 0 para não ou 1 para sim: "))
resposta2 = int(input("\nVocê esteve no local do crime?\nDigite 0 para não ou 1 para sim: "))
resposta3 = int(input("\nVocê mora perto da vítima?\nDigite 0 para não ou 1 para sim: "))
resposta4 = int(input("\nVocê devia para a vítima?\nDigite 0 para não ou 1 para sim: "))
resposta5 = int(input("\nVocê já trabalhou com a vítima?\nDigite 0 para não ou 1 para sim: "))

contador = resposta1 + resposta2 + resposta3 + resposta4 + resposta5

if contador == 5:
    print("\nAssassino")
elif contador == 4 or contador == 3:
    print("\nCúmplice")
elif contador == 2:
    print("\nSuspeita")
else:
    print("\nInocente")
