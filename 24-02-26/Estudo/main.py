class FunçõesAvançadas:
    def __init__(self):
        pass

    def media(self, *args):
        if len(args) == 0:
            return 0
        return sum(args) / len(args)

    def digitarMedia(self):
        while True:
            try:
                numeros = input("Digite os números separados por espaço: ")
                numeros = list(map(int, numeros.split()))
                media_calculada = self.media(*numeros)
                print(f"A média dos números é: {media_calculada}")
                print(f"O maior número é: {max(numeros)}")
                print(f"O menor número é: {min(numeros)}") 
                break
            except ValueError:
                print("Por favor, digite apenas números válidos.")

if __name__ == "__main__":
    funcoes = FunçõesAvançadas()
    funcoes.digitarMedia()