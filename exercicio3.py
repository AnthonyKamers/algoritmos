from modules.ProblemaMochila import *


class Caminhao:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.itens = []


# remover elementos da lista a em b
def remove_common(a, b):
    for item in a:
        if item in b:
            b.remove(item)


# formata itens para print
def print_items(itens):
    itens_parse = [f'({item.item} - {item.peso})' for item in itens]
    print(*itens_parse, sep=', ')


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

        remove_common(selected, itens)

    lucro_total = 0
    for caminhao, resultado in resultado_caminhoes.items():
        lucro_now = resultado[0]
        lucro_total += lucro_now

        print(f'Caminhão de capacidade {caminhao.capacidade} tem lucro {lucro_now}')
        print(f'Itens selecionados: ', end='')

        print_items(resultado[1])
        print()

    print('Itens restantes a serem carregados: ', end='')
    print_items(itens)

    print(f'Lucro total das entregas: {lucro_total}')


if __name__ == "__main__":
    main()
