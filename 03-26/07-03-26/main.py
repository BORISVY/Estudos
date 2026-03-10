class Lista():

    def __init__ (sefl):
        lista = [1, 12, 12, 32, 34, 2, 4, 23, 6, 23]

        #Maior número da lista
        lista_ordenada = sorted(lista)
        print(f"O maior número da lista é: {lista_ordenada[-1]}")

        #Menor número da lista
        print(f"O menor número da lista é: {lista_ordenada[0]}")

        #Média dos números da lista
        media = sum(lista) / len(lista)
        print(f"A média dos números da lista é: {media}")

        #Lista ordenada
        print(f"A lista ordenada é: {lista_ordenada}")

        #Números pares da lista
        pares = [n for n in lista if n % 2 == 0]
        pares_ordenados = sorted(pares)
        print(f"Os números pares da lista são: {pares_ordenados}")

if __name__ =="__main__":
    Lista()