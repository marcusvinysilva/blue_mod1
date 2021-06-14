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
