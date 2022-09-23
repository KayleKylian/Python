class Conta:
    
    def __init__(self, numero, titular, saldo, limite):
        print('Construindo objeto... {}'.format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular}')
    
    def __pode_sacar(self, valor_de_saque):
        valor_disponivel_saque = self.__saldo + self.__limite
        return valor_de_saque <= valor_disponivel_saque

    def sacar(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print('Operação Inválida, Limite Excedido!')
    
    def depositar(self, valor):
        self.__saldo += valor
        
    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
    
    @property
    def limite(self):
        return self.__limite

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo
    
    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    @staticmethod
    def codigo_banco():
        return '001'

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}