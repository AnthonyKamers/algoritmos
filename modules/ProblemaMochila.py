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
    saved = []

    # resolver valor do problema da mochila e salvar itens selecionados em potenciais
    for i, item in enumerate(itens):
        for j in range(capacidade + 1):
            if (item.peso <= j) and (item.valor + M[i - 1][j - item.peso]) > M[i - 1][j]:
                M[i][j] = item.valor + M[i - 1][j - item.peso]
                saved.append((i, j))
            else:
                M[i][j] = M[i - 1][j]

    # encontrar itens selecionados com base em estrutura salva
    selected = []
    j = capacidade
    for i in range(len(itens) - 1, -1, -1):
        item_now = itens[i]
        if (i, j) in saved:
            selected.append(item_now)
            j = j - item_now.peso

    return M[len(itens) - 1][capacidade], selected


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
        assert problema_mochila(itens, capacidade)[0] == 700

    def teste2():
        itens = [
            Item(1, 40, 840),
            Item(2, 30, 600),
            Item(3, 20, 400),
            Item(4, 10, 100),
            Item(5, 20, 300),
        ]
        capacidade = 50
        assert problema_mochila(itens, capacidade)[0] == 1000

    teste1()
    teste2()


if __name__ == "__main__":
    main()
