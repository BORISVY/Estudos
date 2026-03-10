#Sistema Bancário utilizando Python, json e POO
import os
import json

class SistemaBancário():
    def __init__ (self):
        self.contas = []
        self.carregar_contas()

#Carregando informações do arquivo JSON
    def carregar_contas(self):
        if os.path.exists('contas.json'):
            with open('contas.json', 'r', encoding='utf-8') as arq:
                self.contas = json.load(arq)
        
#Criando contas, independente da quantidade de contas
    def criar_contas(self, nome, cpf, saldo_inicial):
        conta = {
            'nome': nome,
            'cpf': cpf,
            'saldo': saldo_inicial
        }
        with open('contas.json', 'w', encoding='utf-8') as arq:
            self.contas.append(conta)
            json.dump(self.contas, arq, indent=4, ensure_ascii=False)
        print(f'Conta criada com sucesso para {nome} com CPF {cpf} e saldo inicial de R${saldo_inicial:.2f}')

#Criando função de deposito
    def depositar(self, cpf, valor):
        if valor <= 0:
            print("Valor inválido para depósito")
            return
        
        try:
            with open('contas.json', 'r', encoding="utf-8") as arq:
                _contas = json.load(arq)
        except FileNotFoundError:
            print("Arquivo de contas não encontrado")
            return
        
        _conta_encontrada = False

        for conta in _contas:
            if conta['cpf'] == cpf:
                conta['saldo'] += valor
                _conta_encontrada = True
                print(f"Depósito de R${valor:.2f} realizado com sucesso!\n Novo saldo: R${conta['saldo']:.2f}")
                break

        if not _conta_encontrada:
            print("CPF não encontrado.")
            return
        
        with open('contas.json', 'w', encoding="utf-8") as arq:
            json.dump(_contas, arq, indent=4, ensure_ascii=False)
            
#Criando função de saque
    def sacar(self, cpf, valor):
        if valor <= 0:
            print("Valor inválido para saque")
            return
        try:
            with open('contas.json', 'r', encoding="utf-8") as arq:
                _contas = json.load(arq)
        except FileNotFoundError:
            print("Arquivo de contas não encontrado")
            return
        
        _conta_encontrada = False

        for conta in _contas:
            if conta['cpf'] == cpf:
                if conta['saldo'] < valor:
                    print("Saldo insuficiente para saque!")
                    return
                
                conta['saldo'] -= valor
                _conta_encontrada = True
                print(f"Saque de R${valor:.2f} realizado com sucesso!\n Novo saldo: R${conta['saldo']:.2f}")
                break

        if not _conta_encontrada:
            print("CPF não encontrado.")
            return
        
        with open('contas.json', 'w', encoding="utf-8") as arq:
            json.dump(_contas, arq, indent=4, ensure_ascii=False)

#Criando função de exibir saldo
    def exibir_saldo(self, cpf):
        try:
            with open('contas.json', 'r', encoding="utf-8") as arq:
                _contas = json.load(arq)
        except FileNotFoundError:
            print("Arquivo de contas não encontrado")
            return
        
        _conta_encontrada = False

        for conta in _contas:
            if conta['cpf'] == cpf:
                _conta_encontrada = True
                print(f"Seu saldo atual é: R${conta['saldo']:.2f}")
                break

        if not _conta_encontrada:
            print("CPF não encontrado.")
            return
        
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
    sistema = SistemaBancário()
    sistema.menu_inicial()
            
