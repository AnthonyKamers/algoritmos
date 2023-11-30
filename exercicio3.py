from modules.ProblemaMochila import *

# https://www.ime.unicamp.br/~mac/db/2015-1S-122181-1.pdf
class Caminhao:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.itens = []


# remover elementos de listas em comum
# https://www.geeksforgeeks.org/remove-common-elements-from-two-list-in-python/
def remove_common(a, b):
    for i in a[:]:
        if i in b:
            a.remove(i)
            b.remove(i)


def main():
    caminhoes = [
        Caminhao(500),
        Caminhao(300),
        Caminhao(350),
        Caminhao(400),
    ]

    itens = [
        Item(1, 400, 500),
        Item(2, 200, 200),
        Item(3, 500, 1500),
        Item(4, 350, 350),
        Item(5, 150, 350),
    ]

    resultado_caminhoes = {}
    for caminhao in caminhoes:
        resultado, selected = problema_mochila(itens, caminhao.capacidade)
        resultado_caminhoes[caminhao] = (resultado, selected)

        remove_common(itens, selected)

    for caminhao, resultado in resultado_caminhoes.items():
        print(f'Caminhão de capacidade {caminhao.capacidade} tem valor {resultado[0]}')
        print(f'Itens selecionados: {[item.item for item in resultado[1]]}')
        print()


if __name__ == "__main__":
    main()
