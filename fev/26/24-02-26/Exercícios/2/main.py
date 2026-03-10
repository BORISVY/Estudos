class usuarios:
    def __init__(self):
        pass

    def criar_usuarios(self, nome, **kwargs):
        self.nome = nome
        self.idade = kwargs.get('idade', None)
        self.email = kwargs.get('email', None)
        self.cidade = kwargs.get('cidade', None)

usuario1 = usuarios()
usuario1.criar_usuarios(nome="Maria", idade=25, email="maria@example.com", cidade="Rio de Janeiro")
usuario2 = usuarios()
usuario2.criar_usuarios(nome="Carlos", idade=40, email="carlos@example.com", cidade="Belo Horizonte")
print(f"Nome: {usuario1.nome}")
print(f"Idade: {usuario1.idade}")
print(f"Email: {usuario1.email}")
print(f"Cidade: {usuario1.cidade}")

print(f"Nome: {usuario2.nome}")
print(f"Idade: {usuario2.idade}")
print(f"Email: {usuario2.email}")
print(f"Cidade: {usuario2.cidade}")

    