from modules.ProblemaMochila import *

class Caminhao:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.itens = []

def main():
    caminhoes = [
        Caminhao(100),
        Caminhao(300),
        Caminhao(50),
        Caminhao(400),
    ]

    itens = [
        Item(1, 400, 500),
        Item(1, 200, 200),
        Item(1, 100, 1500),
        Item(1, 350, 350),
        Item(1, 150, 350),
    ]

    for caminhao in caminhoes:
        print(problema_mochila(itens, caminhao.capacidade))


if __name__ == "__main__":
    main()
