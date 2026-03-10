import json
import os

class CadastroDeProdutos():
    def __init__(self):
        self.arquivo = "dicionario.json"
        self.lista_produtos = self.carregar_dados()

    def carregar_dados(self):

        """ Usado para carregar os dados do arquivo .json caso ele já existir, impedido
        a criação de um novo arquivo
        """

        if os.path.exists(self.arquivo):
            try: 
                with open(self.arquivo, "r", encoding="utf-8") as arq:
                    return json.load(arq)
            except json.JSONDecodeError:
                return []
        return []

    def adicionar_produto(self, nome, preço, quantidade):

        """ Função para adicionar produtos ao sistema. Recebe as informações dele
        e realiza o cadastro no arquivo .json
        """

        produto = {
            "Nome": nome,
            "Preço": preço,
            "Quantidade":quantidade
        }
        self.lista_produtos.append(produto)
        self.salvar()
        print(f"Produto {nome} adicionado com sucesso!")

    def salvar(self):

        """ Função usada para salvar as informaçoes no arquivo .json ou para criar
        o arquivo, caso ele ainda não exista
        """

        with open("dicionario.json", "w", encoding="utf-8") as arq:
            json.dump(self.lista_produtos, arq, indent=4, ensure_ascii=False)
    
    def listar_produtos(self):
        
        """ Função que exibe uma listagem dos produtos cadastrados no arquivo .json
        """

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

        """ Função que exibe uma somatoria da quantidade total de estoque
        """

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