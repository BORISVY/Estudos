import os
import json

class SistemaBancário:
    def __init__(self):
        os.system('clear')
        while True:
            print("Bem-vindo ao Sistema Bancário!")
            print("Menu de opções:")
            print("1. Criar conta")
            print("2. Depositar")
            print("3. Sacar")
            print("4. Ver saldo")
            print("5. Sair")
            try: 
                self.opcao = int(input("Digite a opção desejada:"))
                if self.opcao == 1:
                    self.criar_conta()
                elif self.opcao == 2:
                    self.depositar()
                elif self.opcao == 3:
                    self.sacar()
                elif self.opcao == 4:
                    self.ver_saldo()
                elif self.opcao == 5:
                    print("Obrigado por usar o Sistema Bancário. Até logo!")
                    break
                else:
                    print("Opção inválida. Por favor, tente novamente.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número correspondente à opção desejada.")

    def conta_bancaria(self, nome, saldo_inicial):
        self.nome = nome
        self.saldo = saldo_inicial

    def criar_conta(self):
        os.system('clear')
        nome = input("Digite o nome do titular da conta:")
        saldo_inicial = float(input("Digite o saldo inicial da conta:"))  
        with open('conta_bancaria.json', 'w', encoding='utf-8') as arquivo:
            json.dump({'nome': nome, 'saldo': saldo_inicial}, arquivo)
        self.conta_bancaria(nome, saldo_inicial)
        print(f"Conta criada com sucesso para {nome} com saldo inicial de R${saldo_inicial:.2f}")
        

    def depositar(self):
        os.system('clear')
        valor_deposito = float(input("Digite o valor a ser depositado:"))
        with open('conta_bancaria.json', 'r', encoding='utf-8') as arquivo:
            conta = json.load(arquivo)
        conta['saldo'] += valor_deposito
        with open('conta_bancaria.json', 'w', encoding='utf-8') as arquivo:
            json.dump(conta, arquivo)   
        self.saldo += valor_deposito
        print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}")

    def sacar(self):
        os.system('clear')
        valor_saque = float(input("Digite o valor a ser sacado:"))
        if valor_saque > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
        else:
            with open('conta_bancaria.json', 'r', encoding='utf-8') as arquivo:
                conta = json.load(arquivo)
            conta['saldo'] -= valor_saque
            self.saldo -= valor_saque
            with open('conta_bancaria.json', 'w', encoding='utf-8') as arquivo:
                json.dump(conta, arquivo)
            print(f"Saque de R${valor_saque:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}")

    def ver_saldo(self):
        os.system('clear')
        with open('conta_bancaria.json', 'r', encoding='utf-8') as arquivo:
            conta = json.load(arquivo)
        self.saldo = conta['saldo']
        print(f"Saldo atual da conta de {self.nome}: R${self.saldo:.2f}")

if __name__ == "__main__":
    SistemaBancário()       