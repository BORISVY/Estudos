class ContaBancaria():
    def __init__(self, titular, __saldo):
        self.titular = titular
        self.__saldo = __saldo

    def depositar(self, valor):
        self.__saldo += valor   
        print(f"Depósito de R${valor} realizado com sucesso. Saldo atual: R${self.__saldo}")

    def sacar(self, valor):
        if valor > self.__saldo:
            print("Saldo insuficiente para realizar o saque.")
        else:
            self.__saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso. Saldo atual: R${self.__saldo}")
    
    def mostrar_saldo(self):
        print(f"Saldo atual: R${self.__saldo}")

# Criando uma conta bancária
conta = ContaBancaria("João Silva", 1000)
# Exibindo o saldo inicial
conta.mostrar_saldo()
# Realizando um depósito
conta.depositar(500)
# Realizando um saque
conta.sacar(200)
# Exibindo o saldo final
conta.mostrar_saldo()

