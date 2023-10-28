import sys

from modules.Grafo1 import Grafo


class VerticeDFS:
    def __init__(self, vertice):
        self.vertice = vertice
        self.hasPassed = False
        self.tempo = sys.float_info.max
        self.final = sys.float_info.max


def ordenacao_topologica(grafo):
    vertices = criar_verticesDFS(grafo)

    tempo = 0  # tempo de início
    O = []  # lista O de ordenamento topológico
    for vertice in vertices:
        if vertice.hasPassed == False:
            vertices, tempo = DFS_visit_ot(vertice, vertices, tempo, O)

    # printtar no formato do exercício
    O = list(map(lambda x: x.vertice.rotulo, O))
    print(*O, sep=" -> ", end=". \n")


def DFS_visit_ot(verticeOrigem, vertices, tempo, O):
    indexVerticeOrigem = int(verticeOrigem.vertice.id) - 1

    vertices[indexVerticeOrigem].hasPassed = True
    tempo += 1
    vertices[indexVerticeOrigem].tempo = tempo

    for vizinho in verticeOrigem.vertice.vizinhosSaida():
        if vertices[vizinho].hasPassed == False:
            vertices, tempo = DFS_visit_ot(vertices[vizinho], vertices, tempo, O)

    tempo += 1
    vertices[indexVerticeOrigem].final = tempo

    # adiciona vértice v no início da lista O
    O.insert(0, vertices[indexVerticeOrigem])

    return vertices, tempo


def criar_verticesDFS(grafo):
    return [VerticeDFS(vertice) for vertice in grafo.grafo]


def main():
    grafo = Grafo()
    grafo.ler("../testes/dirigidos/teste3.net")
    ordenacao_topologica(grafo)


if __name__ == "__main__":
    main()
