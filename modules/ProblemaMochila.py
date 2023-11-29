class Item:
    def __init__(self, item, peso, valor):
        self.item = item
        self.peso = peso
        self.valor = valor


def problema_mochila(itens, capacidade):
    def cria_memorizacao():
        memoria = []
        for i in range(len(itens)):
            linha = []
            for j in range(capacidade + 1):
                linha.append(0)
            memoria.append(linha)
        return memoria

    M = cria_memorizacao()
    for i, item in enumerate(itens):
        for w in range(capacidade + 1):
            if w < item.peso:
                M[i][w] = M[i - 1][w]
            else:
                valor_anterior = M[i - 1][w]
                valor_item = M[i - 1][w - item.peso] + item.valor
                M[i][w] = max(valor_anterior, valor_item)

    return M[len(itens) - 1][capacidade]


def main():
    def teste1():
        itens = [
            Item(1, 3, 100),
            Item(2, 5, 150),
            Item(3, 7, 450),
            Item(4, 1, 50),
            Item(5, 2, 200),
        ]
        capacidade = 10
        assert problema_mochila(itens, capacidade) == 700

    def teste2():
        itens = [
            Item(1, 40, 840),
            Item(2, 30, 600),
            Item(3, 20, 400),
            Item(4, 10, 100),
            Item(5, 20, 300),
        ]
        capacidade = 50
        assert problema_mochila(itens, capacidade) == 1000

    teste1()
    teste2()


if __name__ == "__main__":
    main()