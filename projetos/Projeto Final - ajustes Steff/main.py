from dia import Dia
from personagem import Personagem
from arma import Arma
from aventuras import Aventuras
from contador import Contador
from asciis import Asciis
import pygame
import os
import time

if(__name__ == "__main__"):
    while True:
        contador = Contador()

        Asciis.bemVindo()
        inicio_jogo = ('Para começar vamos construir seu personagem....')
        for ch in inicio_jogo:
            time.sleep(0.1) 
            print(ch, end='', flush=True)
        print()
        Personagem.personagem(Personagem,'nome','sexo','cor_olhos','cor_cabelo',contador)

        print()
        inicio_dia = ('Amanheceu... Está um dia: ')
        for ch in inicio_dia:
            time.sleep(0.1) 
            print(ch, end='', flush=True)
        escolha_dia = input('\n1 - Dia Bom\n2 - Dia Frio\nEscolha uma opção:')
        while escolha_dia not in ['1','2']:
            print('Opção inválida!')
            escolha_dia = input('\n1 - Dia Bom\n2 - Dia Frio\nEscolha uma opção:')
        Dia.dia_bom_ruim(escolha_dia)

        
        Arma.escolha_arma(Arma, 'arma', contador)

        
        print()
        escolhe_aventura = input('1 - Praia\n2 - Montanha\nEscolha o local da sua aventura:')
        while escolhe_aventura not in ['1','2']:
            print('Opção inválida!')
            escolhe_aventura = input('1 - Praia\n2 - Montanha\nEscolha o local da sua aventura:')
        if escolhe_aventura == '1':
            Aventuras.AventPraia(Aventuras,'monstro',contador)
        elif escolhe_aventura == '2':
            Aventuras.AventMontanha(Aventuras, 'viagem_tempo',contador)

        print()
        continuar = input('Deseja jogar novamente? [S/N]: ').upper()[0]
        while continuar not in 'SN':
            continuar = input('Deseja jogar novamente? [S/N]: ').upper()[0]
        if continuar == 'N':
            break
    print()
    print('O jogo foi encerrado pelo usuário.')
    Asciis.final()