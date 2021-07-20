# a. Crie uma classe chamada bombaCombustível, com no mínimo esses atributos:
# i. tipoCombustivel.
# ii. valorLitro.
# iii. quantidadeCombustivel.
# b. A classe deve possuir no mínimo esses métodos:
# i. abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que
# foi colocada no veículo.
# ii. abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor
# a ser pago pelo cliente.
# iii. alterarValor( ) – altera o valor do litro do combustível.
# iv. alterarCombustivel( ) – altera o tipo do combustível.
# v. alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.

class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self):
        valor = float(input('Informe o valor que deve ser colocado de combustível: ').replace(',','.'))
        quantLitrosRecebida = valor / self.valorLitro
        self.quantidadeCombustivel -= quantLitrosRecebida
        print(f'Você recebeu {quantLitrosRecebida} litros')

    def abastecerPorLitro(self):
        litros = float(input('Informe quantos litros de combustível você quer: ').replace(',','.'))
        valorQueDeveSerPago = litros * self.valorLitro
        self.quantidadeCombustivel -= litros
        print(f'Você deve pagar R${valorQueDeveSerPago}')

    def alterarValor(self):
        novoValor = float(input('Informe o novo valor do combustivel: ').replace(',','.'))
        self.valorLitro = novoValor

    def alterarCombustivel(self):
        novoCombustivel = input('Informe o novo tipo de combustivel para essa bomba: ').lower()
        self.tipoCombustivel = novoCombustivel

    def alterarQuantidadeCombustivel(self):
        novaQuant = float(input('Informe a nova quantidade de combustivel nessa bomba: '))
        self.quantidadeCombustivel = novaQuant