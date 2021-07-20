# 2) Crie uma classe chamada Conta para simular as operações de uma conta corrente. Sua classe deverá ter os atributos Titular e Saldo, e os métodos Sacar e Depositar. Crie um objeto da classe Conta e teste os atributos e métodos implementados.
class Conta():
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo

    def sacar(self,valor_saque):
        self.saldo -= valor_saque
        print(f'Seu saldo atual é: {self.saldo}')

    def depositar(self,valor_deposito):
        self.saldo -= valor_deposito
        print(f'Seu saldo atual é: {self.saldo}')

# sacar = Conta('Marcus',10000)
# sacar.sacar(3500)

