from asciis import Asciis

class Arma:
    def escolha_arma(self, escolha_arma, contador):
        print()
        print('Escolha uma arma para a sua aventura: ')
        print()
        dic_arma = {'1':'Espingarda','1':'Arco e Flecha','3':'Espada','4':'Sabre de Luz','5':'Foice','6':'Tridente de Poseidon'}
        for c,v in dic_arma.items():
            print(f'[{c}] {v}')
        escolha_arma = input('Digite a sua opção: ')
        while escolha_arma not in ['1','2','3','4','5','6']:
            print()
            print('Opção inválida!')
            escolha_arma = input('Digite a sua opção: ')
        if escolha_arma == '1':
            contador.incrementar(5)
            print()
            print('Você escolheu ESPINGARDA. Esperamos que saiba atirar... ')
        elif escolha_arma == '2':
            contador.incrementar(15)
            print()
            print('Você escolheu ARCO E FLECHA. Esperamos que tenha uma boa mira... ')
        elif escolha_arma == '3':
            contador.incrementar(25)
            print()
            print('Você escolheu ESPADA. Esperamos que você seja habilidoso... ')
        elif escolha_arma == '4':
            contador.incrementar(20)
            print()
            print('Você escolheu SABRE DE LUZ. Esperamos QUE A FORÇA ESTEJA COM VOCÊ... ')
        elif escolha_arma == '5':
            contador.incrementar(30)
            print()
            print('Você escolheu FOICE. TODO MUNDO EM PÂNICO AGORA... ')
        elif escolha_arma == '6':
            contador.incrementar(50)
            print()
            print('Você escolheu TRIDENTE DE POSEIDON. Esperamos que saiba nada... Continue a nadar...continue a nadar... ')
            Asciis.dory()
        