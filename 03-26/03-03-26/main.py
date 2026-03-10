import os
import json

FILENAME = "contas.json"

class Conta:
    def __init__(self, nome, cpf, saldo=0.0):
        self.__nome = nome
        self.__cpf = cpf
        self.__saldo = saldo

    @property
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def saldo(self):
        return self.__saldo
    
    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("Valor inválido para depósito")
        self.__saldo += valor

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("Valor inválido para saque.")
        if self.__saldo < valor:
            raise ValueError("Saldo insuficiente.")
        self.__saldo -= valor

    def para_dicionario(self):
        return{
            "nome": self.__nome,
            "cpf": self.__cpf,
            "saldo": self.__saldo
        }
    
    @classmethod
    def do_dicionario(cls, dados):
        return cls(dados["nome"], dados["cpf"], dados["saldo"])
    
class RepositorioDeContas:
    def __init__(self, arquivo=FILENAME):
        self.arquivo = arquivo
        self.contas: list[Conta] = []
        self.carregar_contas()

    def carregar_contas(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, "r", encoding="utf-8") as arq:
                dados = json.load(arq)
                self.contas = [Conta.do_dicionario(c) for c in dados]
        else:
            self.contas = []

    def salvar_contas(self):
        with open(self.arquivo, "w", encoding="utf-8") as arq:
            json.dump([c.para_dicionario() for c in self.contas], arq, indent=4, ensure_ascii=False)
    
    def buscar_cpf(self, cpf):
        for conta in self.contas:
            if conta.cpf == cpf:
                return conta
        return None
    
class SistemaBancario:
    def __init__(self, repositorio=None):
        self.repo = repositorio or RepositorioDeContas()

    def criar_contas(self, nome, cpf, saldo_inicial):
        if self.repo.buscar_cpf(cpf):
            print("CPF já cadastrado!")
            return
        
        conta = Conta(nome, cpf, saldo_inicial)
        self.repo.contas.append(conta)
        self.repo.salvar_contas()
        print(f'Conta criada com sucesso para {nome} com CPF {cpf} e saldo inicial de R${saldo_inicial:.2f}')    

    def depositar(self, cpf, valor):
        conta = self.repo.buscar_cpf(cpf)
        if not conta:
            print("CPF não encontrado!")
            return
        try:
            conta.depositar(valor)
            self.repo.salvar_contas()
            print(f"Depósito realizado com sucesso! O saldo atual é de R$ {conta.saldo:.2f}")
        except ValueError as e:
            print(e)

    def sacar(self, cpf, valor):
        conta = self.repo.buscar_cpf(cpf)
        if not conta:
            print("CPF não encontrado!")
            return
        try:
            conta.sacar(valor)
            self.repo.salvar_contas()
            print(f"Saque realizado com sucesso! O seu saldo atual é R$ {conta.saldo:.2f}")
        except ValueError as e:
            print(e)

    def exibir_saldo(self,cpf):
        conta = self.repo.buscar_cpf(cpf)
        if conta:
            print(f"O saldo atual é: R$ {conta.saldo:.2f}")
        else:
            print("CPF não encontrado!")

    def menu_inicial(self):
            import os
            import time
            os.system('clear')
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
                    nome = input("Digite o nome do titular da conta\n")
                    cpf = input("Digite o CPF do titular da conta:\n")
                    saldo_inicial = float(input("Digite o saldo inicial da conta:\n"))
                    self.criar_contas(nome, cpf, saldo_inicial)

                elif opt == "2":
                    os.system('clear')
                    cpf = input("Digite o CPF da conta que deseja realizar o deposito:\n ")
                    valor = float(input("Digite o valor do depósito:\n "))
                    self.depositar(cpf, valor)

                elif opt == "3":
                    os.system('clear')
                    cpf = input("Digite o CPF da conta que deseja realizar o saque:\n ")
                    valor = float(input("Digite o valor do saque:\n "))
                    self.sacar(cpf, valor)

                elif opt == "4":
                    os.system('clear')
                    cpf = input("Digite o CPF da conta que deseja consultar o saldo:\n ")
                    self.exibir_saldo(cpf)

                elif opt == "5":
                    os.system('clear')
                    print("Saindo do sistema...")
                    break

                else:
                    print("Opção inválida.")

if __name__ == "__main__":
    sistema = SistemaBancario()
    sistema.menu_inicial()