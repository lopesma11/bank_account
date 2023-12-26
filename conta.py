
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto...")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de R$ {} do(a) titular {}".format(self.__saldo, self.__titular))

    def deposito(self, valor):
        self.__saldo += valor

    def __saque_permitido(self, valor_a_sacar):
        valor_disponivel_para_saque = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_para_saque

    def saque(self, valor):
        if self.__saque_permitido(valor):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))
    def transferencia(self, valor, conta_destino):
        self.saque(valor)
        conta_destino.deposito(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {"BB": "001", "Caixa": "104", "Bradesco":"237"}

