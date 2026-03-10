import os
import json

arquivo = "contas.json"

class Conta():

    def __init__ (self, nome, cpf, saldo=0.0, arq=arquivo):
        self.__nome = nome
        self.__cpf = cpf
        self.__saldo = saldo
        self.arq = arq
        self.contas: [] # type: ignore
        

    @property
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def saldo(self):
        return self.__saldo
    
    def colocar_na_lista(self):
        return{
            "nome": self.__nome,
            "cpf": self.__cpf,
            "saldo": self.__saldo
        }
    
    @classmethod
    def retirar_da_lista(cls, dados):
        return cls(dados["nome"], dados["cpf"], dados["saldo"])
    
    def buscar_cpf(self, cpf):
        for conta in self.contas:
            if conta.cpf == cpf:
                return conta
        return None
    
    def carregar_contas(self):
        if os.path.exists(self.arq):
            with open(self.arq, "r", encoding="utf-8") as arq:
                dados = json.load(arq)
                self.contas = [Conta.retirar_da_lista(c) for c in dados]
        else:
            self.contas = []

    def salvar(self):
        with open(self.arq, "w", encoding="utf-8") as arq:
            json.dump([c.colocar_na_lista() for c in self.contas], arq, indent=4, ensure_ascii=False)

    def criar_contas(self,nome, cpf, saldo_inicial):
        if self.buscar_cpf(cpf):
            print("CPF já cadastrado!")
            return
        
        conta = Conta(nome, cpf, saldo_inicial)
        self.contas.append(conta)
        self.salvar()
        print(f"Conta criada com sucesso para {nome} com CPF {cpf} e saldo inicial de R$ {saldo_inicial:.2f}")
    
    def depositar(self, cpf, valor):
        conta = self.buscar_cpf(cpf)
        if not conta:
            print("CPF não encontrado!")
            return
        try:
            if valor <= 0:
                raise ValueError("Valor inválido para depósito")
            conta._Conta__saldo += valor
            self.salvar()
            print(f"Depósito realizado com sucesso! Seu saldo atual é de R$ {conta.saldo:.2f}")
        except ValueError as e:
            print(e)

    def sacar(self, cpf, valor):
        conta = self.buscar_cpf(cpf)
        if not conta:
            print("CPF não encontrado!")
            return
        try:
            if valor <= 0:
                raise ValueError("Valor inválido para saque.")
            if conta.saldo < valor:
                raise ValueError("Saldo insuficiente!")
            conta._Conta__saldo -= valor
            self.salvar()
            print(f"Saque realizado com sucesso! Seu sando atual é de R$ {conta.saldo:.2f}")
        except ValueError as e:
            print(e)

    def exibir_saldo(self, cpf):
        conta = self.buscar_cpf(cpf)
        if conta:
            print(f"O saldo atual é: R$ {conta.saldo:.2f}")
        else:
            print("CPF não encontrado!")

class SistemaBancario():
    import os
    os.system('clear')
    def __init__(self):
        self.conta = Conta("", "")
        self.conta.carregar_contas()
        while True:
            print("____________________________ SISTEMA BANCÁRIO ____________________________")
            print("Selecione a opção do menu:")
            print("1 - Cadastrar Nova Conta Bancária")
            print("2 - Realizar Deposito em Conta")
            print("3 - Realizar Saque em Conta")
            print("4 - Visualizar Saldo")
            print("5 - Sair")

            opt = input("Escolha uma opção:")

            if opt == "1":
                os.system('clear')
                nome = input("Digite o nome do titular da conta:")
                cpf = input("Digite o CPF do titular da conta:")
                saldo_inicial = float(input("Digite o saldo inicial da conta:"))
                self.conta.criar_contas(nome, cpf, saldo_inicial)

            elif opt == "2":
                os.system('clear')
                cpf = input("Digite o CPF da conta que deseja realizar o deposito:\n ")
                valor = float(input("Digite o valor do depósito:\n "))
                self.conta.depositar(cpf, valor)

            elif opt == "3":
                os.system('clear')
                cpf = input("Digite o CPF da conta que deseja realizar o saque:\n ")
                valor = float(input("Digite o valor do saque:\n "))
                self.conta.sacar(cpf, valor)

            elif opt == "4":
                os.system('clear')
                cpf = input("Digite o CPF da conta que deseja consultar o saldo:\n ")
                self.conta.exibir_saldo(cpf)

            elif opt == "5":
                os.system('clear')
                print("Saindo do sistema...")
                break

            else:
                print("Opção inválida.")

if __name__ =="__main__":
    SistemaBancario()