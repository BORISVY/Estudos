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

    def ordena_valor(self):
        """ Função que irá exibir uma lista com todos os produtos em ordem crecente de valor
        """
        if not self.lista_produtos:
            print("Nenhum produto cadastrado!")
            return
        os.system("clear")
        print("---Lista dos Produtos Ordenados por Valor---")
        self.lista_produtos.sort(key=lambda prod: prod["Preço"])
        for produto in self.lista_produtos:
            print(f"Produto: {produto["Nome"]} | Preço: R$ {produto["Preço"]:.2f} | Estoque: {produto["Quantidade"]}")
        return

    def ordena_qtd(self):
        """ Função que irá exibir uma lista com todos os produtos em ordem crecente de quantidade
        """
        if not self.lista_produtos:
            print("Nenhum produto cadastrado!")
            return
        os.system("clear")
        print("---Lista dos Produtos Ordenados por Quantidade---")
        self.lista_produtos.sort(key=lambda prod: prod["Quantidade"])
        for produto in self.lista_produtos:
            print(f"Produto: {produto["Nome"]} | Preço: R$ {produto["Preço"]:.2f} | Estoque: {produto["Quantidade"]}")
        return  

    def buscar_produtos(self, nome_busca):

        """ Função para consulta e localização de um produto na lista
        """

        for produto in self.lista_produtos:
            if produto.get("Nome") == nome_busca:
                nome = produto.get("Nome")
                preço = produto.get("Preço")
                qtd = produto.get("Quantidade")
                print(f"Produto: {nome} | Preço: {preço} | Estoque: {qtd}")
                return
        print("Produto não encontrado") 
            
    def total_estoque(self):

        """ Função que exibe uma somatoria da quantidade total de estoque
        """

        if not self.lista_produtos:
            print("Nenhum produto cadastrado!")
            return
        os.system("clear")
        print("Quantidade Total de Estoque")
        estoque_total = 0
        for produto in self.lista_produtos:
            for chave, valor in produto.items():
                if chave == "Quantidade":
                    estoque_total += valor
        print(f"{estoque_total}")
        return estoque_total
    
    def total_valor(self):

        """ Função que exibe uma somatoria do valor total de estoque
        """

        if not self.lista_produtos:
            print("Nenhum produto cadastrado!")
            return
        os.system("clear")
        print("Valor Total de Estoque")
        valor_total = 0
        for produto in self.lista_produtos:
            for chave, valor in produto.items():
                if chave == "Preço":
                    valor_total += valor
        print(f"{valor_total}")
        return valor_total
        
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
            print("4 - Imprima Valor de Estoque Total")
            print("5 - Localizar Produto")
            print("6 - Relatório Filtrado de Produtos")
            print("7 - Sair")
            opt = input("Escolha uma opção:")

            if opt == "1":
                os.system('clear')
                nome = input("Digite o nome do produto:")
                while True:
                    try:
                        preço = float(input("Digite o preço do produto:"))
                        break
                    except ValueError:
                        print("Erro: Digite apenas números válidos (ex: 10.50)")
                while True:
                    try:
                        quantidade = float(input("Digite o estoque inicial desse produto:"))
                        if quantidade < 0:
                            print("Erro: A quantidade não pode ser negativa!")
                            continue
                        break
                    except ValueError: 
                        print("Erro: Digite apenas números!")
                self.prod.adicionar_produto(nome, preço, quantidade)

            elif opt == "2":
                os.system('clear')
                self.prod.listar_produtos()

            elif opt == "3":
                os.system('clear')
                self.prod.total_estoque()

            elif opt == "4":
                os.system('clear')
                self.prod.total_valor()    

            elif opt == "5":
                os.system('clear')
                nome = input("Digite o nome do produto:")
                self.prod.buscar_produtos(nome)

            elif opt == "6":
                os.system('clear')
                print("Relatório Filtrado de Produtos")
                print("1 - Produtos Ordenados por Valor")
                print("2 - Produtos Ordenados por Quantidade de Estoque")
                opt2 = input("Seleciona a opção de filtro desejada:")

                if opt2 == "1":
                    os.system('clear')
                    self.prod.ordena_valor()

                elif opt2 == "2":
                    os.system('clear')
                    self.prod.ordena_qtd()    

                else:
                    print("Opção inválida.")    
                    
            elif opt == "7":
                os.system('clear')
                print("Saindo do sistema...")
                break

            else:
                print("Opção inválida.")

if __name__ =="__main__":
    Menu()