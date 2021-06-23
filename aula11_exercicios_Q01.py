# 1 – Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6, 7, e 9 (que podem ser armazenados em uma lista) e seus valores correspondentes aos quadrados desses números.

lista_num = [1, 4, 5, 6, 7, 9]
dic_num_quadrado = {}

for n in lista_num:
    dic_num_quadrado[n] = n**2

print(dic_num_quadrado)


# b – Crie um dicionário em que suas chaves correspondem a números inteiros entre [1, 10] e cada valor associado é o número ao quadrado.​

num = int(input('Digite um número inteiro: '))
dic_quadrado = dict()

for i in range(1, num+1):
    dic_quadrado[i] = i**2
    
print(dic_quadrado)