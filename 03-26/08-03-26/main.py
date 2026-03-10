import json
import os

class CadastroDeProdutos():
    def __init__(self):
        self.arquivo = "dicionario.json"
        self.lista_produtos = self.carregar_dados()

    def carregar_dados(self):
        if os.path.exists(self.arquivo):
            try: 
                with open(self.arquivo, "r", encoding="utf-8") as arq:
                    return json.load(arq)
            except json.JSONDecodeError:
                return []
        return []

    def adicionar_produto(self, nome, preço, quantidade):
        produto = {
            "Nome": nome,
            "Preço": preço,
            "Quantidade":quantidade
        }
        self.lista_produtos.append(produto)
        self.salvar()
        print(f"Produto {nome} adicionado com sucesso!")

    def salvar(self):
        with open("dicionario.json", "w", encoding="utf-8") as arq:
            json.dump(self.lista_produtos, arq, indent=4, ensure_ascii=False)
    
    def listar_produtos(self):
        if not self.lista_produtos:
            print("Nenhum produto cadastrado!")
            return
        os.system("clear")
        print("---Lista dos Produtos Cadastrados---")
        for produto in self.lista_produtos:
            nome = produto.get("Nome")
            preço = produto.get("Preço")
            qtd = produto.get("Quantidade")

            print(f"Produto: {nome} | Preço: {preço} | Estoque: {qtd}")

    def total_estoque(self):
        if not self.lista_produtos:
            print("Nenhum produto cadastrado!")
            return
        os.system("clear")
        print("Quantidade total de estoque")
        total = 0
        for produto in self.lista_produtos:
            for chave, valor in produto.items():
                if chave == "Quantidade":
                    total += valor
        print(f"{total}")
        return total
        
class Menu():
    import os
    os.system('clear')
    def __init__(self):
        self.prod = CadastroDeProdutos()
        while True:
            print("____________________________ SISTEMA DE ESTOQUE ____________________________")
            print("Selecione a opção do menu:")
            print("1 - Cadastrar Produto")
            print("2 - Listar Produtos")
            print("3 - Imprimir Estoque Total")
            print("4 - Sair")
            opt = input("Escolha uma opção:")

            if opt == "1":
                os.system('clear')
                nome = input("Digite o nome do produto:")
                preço = float(input("Digite o preço do produto:"))
                quantidade = float(input("Digite o estoque inicial desse produto:"))
                self.prod.adicionar_produto(nome, preço, quantidade)

            elif opt == "2":
                os.system('clear')
                self.prod.listar_produtos()

            elif opt == "3":
                os.system('clear')
                self.prod.total_estoque()

            elif opt == "4":
                os.system('clear')
                print("Saindo do sistema...")
                break

            else:
                print("Opção inválida.")

if __name__ =="__main__":
    Menu()