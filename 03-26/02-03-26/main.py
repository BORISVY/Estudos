#Sistema Bancário utilizando Python, json e POO
import os
import json

FILENAME = "contas.json"

class Conta(dict):
    pass

class RepositorioDeContas:
    def __init__(self, arquivo=FILENAME):
        self.arquivo = arquivo
        self.contas: list[Conta] = []
        self.carregar_contas()

#Carregando informações do arquivo JSON
    def carregar_contas(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, 'r', encoding='utf-8') as arq:
                self.contas = [Conta(c) for c in json.load(arq)]
        else:
            self.contas = []

    def salvar_contas(self):
        with open(self.arquivo, "w", encoding="utf-8") as arq:
            json.dump(self.contas, arq, indent=4, ensure_ascii=False)
    
    def buscar_cpf(self, cpf):
        for conta in self.contas:
            if conta["cpf"] == cpf:
                return conta
        return None
    
    def adicionar(self, conta: Conta):
        self.contas.append(conta)
        self.salvar_contas()

class SistemaBancario:
    def __init__(self, repositorio=None):
        self.repo = repositorio or RepositorioDeContas()
        
#Criando contas, independente da quantidade de contas
    def criar_contas(self, nome, cpf, saldo_inicial):
        if self.repo.buscar_cpf(cpf):
            print("CPF já cadastrado!")
            return
        conta = Conta(nome=nome, cpf=cpf, saldo=saldo_inicial)
        self.repo.adicionar(conta)
        print(f'Conta criada com sucesso para {nome} com CPF {cpf} e saldo inicial de R${saldo_inicial:.2f}')

#Criando função de deposito
    def depositar(self, cpf, valor):
        if valor <= 0:
            print("Valor inválido para depósito")
            return
        conta = self.repo.buscar_cpf(cpf)
        if not conta:
            print("CPF não encontrado!")
            return
        conta["saldo"] += valor
        self.repo.salvar_contas()
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso! O saldo da conta atual é de R$ {conta['saldo']:.2f}")
        
            
#Criando função de saque
    def sacar(self, cpf, valor):
        if valor <= 0:
            print("Valor inválido para saque")
            return
        conta = self.repo.buscar_cpf(cpf)
        if not conta:
            print("CPF não encontrado.")
            return
        if conta["saldo"] < valor:
            print("Saldo insuficiente")
            return
        conta["saldo"] -= valor
        self.repo.salvar_contas()
        print(f"Saque de R${valor:.2f} realizado com sucesso! O novo saldo da conta é R${conta['saldo']:.2f}")

#Criando função de exibir saldo
    def exibir_saldo(self, cpf):
        conta = self.repo.buscar_cpf(cpf)
        if conta:
            print(f"Saldo: R${conta['saldo']:.2f}")
        else:
            print("CPF não encontrado.")


        
#Criando menu 

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
            
