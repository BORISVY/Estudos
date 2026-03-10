class usuários():
    def __init__(self):
        pass

    def exibir_dados(self, **kwargs):
        print(f"Nome: {kwargs['nome']}")
        print(f"Idade: {kwargs['idade']}")
        print(f"Cidade: {kwargs['cidade']}")

usuario1 = usuários()
usuario1.exibir_dados(nome="João", idade=30, cidade="São Paulo")


