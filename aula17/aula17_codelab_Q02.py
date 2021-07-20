# Crie um programa que gerencie o aproveitamento de um jogador de futebol; o programa vai ler o nome do jogador e quantas partidas ele jogou.Depois vai ler a quantidade de gols feito em cada partida. No final tudo isso será guardado em um dicionário incluindo o total de gols feitos durante o campeonato.

'''campeonato = {}
nome = input('Digite o nome do jogador: ')
partidas = int(input(f'Informe quantas partidas {nome} jogou: '))
lista_gols = []
lista_total_gols = []

for i in range(partidas):
    gols = int(input(f'Quantos gols {nome} fez na {i+1}ª partida? '))
    lista_gols.append(gols)

lista_total_gols.append(f'{sum(lista_gols)} gols no campeonato')
lista_gols.append(lista_total_gols)
lista_gols.append(f'{partidas} partidas')
campeonato[nome] = lista_gols
print()
print(campeonato)'''

# Vamos aprimorar o código:  cadastro de jogador de futebol.py que foi desenvolvido no Code Lab da aula 14. Faça com que o seu código funcione para vários jogadores, incluindo um sistema de visualização de detalhes de aproveitamento de cada jogador. 
class cadastro():
    def __init__(self,nome,partida,gol):
        self.nome = nome
        self.partida = partida
        self.gol = gol
    