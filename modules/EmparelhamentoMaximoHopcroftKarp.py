import sys

from modules.Grafo1 import Grafo


def BFS(grafo, mate, distancia, X):
    fila = []

    for x in X:
        if mate[x] is None:
            distancia[x] = 0
            fila.append(x)
        else:
            distancia[x] = sys.float_info.max

    distancia[None] = sys.float_info.max

    while len(fila) != 0:
        x = fila.pop()

        if distancia[x] < distancia[None]:
            for y in grafo.vizinhosSaida(x):
                y += 1
                if distancia[mate[y]] == sys.float_info.max:
                    distancia[mate[y]] = distancia[x] + 1

                    fila.append(mate[y])

    return distancia[None] != sys.float_info.max


def DFS(grafo, mate, x, distancia):
    if x != None:
        for y in grafo.vizinhosSaida(x):
            y += 1
            if distancia[mate[y]] == distancia[x] + 1:
                if DFS(grafo, mate, mate[y], distancia):
                    mate[y] = x
                    mate[x] = y
                    return True
        distancia[x] = sys.float_info.max
        return False
    return True


def hopcroft_karp(grafo):
    distancia = {}
    mate = {}

    # inicializando as estruturas
    for vertice in grafo.grafo:
        distancia[vertice.id] = sys.float_info.max
        mate[vertice.id] = None

    # definindo X (aqui pegaremos a primeira metade dos vértices)
    qtd_vertices = grafo.qtdVertices()
    qtd_x = qtd_vertices / 2
    X = []
    for k, vertice in enumerate(grafo.grafo):
        if k < qtd_x:
            X.append(vertice.id)

    # Tamanho do emparelhamento
    m = 0
    while BFS(grafo, mate, distancia, X):
        for x in X:
            if mate[x] is None:
                if DFS(grafo, mate, x, distancia):
                    m += 1

    # printtar no formato do exercício
    # valor do emparelhamento máximo
    print(m)

    # arestas do emparelhamento máximo
    string = ""
    for x in X:
        string += f'{x}-{mate[x]},'
    print(string[:-1])


def main():
    grafo = Grafo()
    grafo.ler("../testes/emparelhamento_maximo/pequeno.net")
    hopcroft_karp(grafo)


if __name__ == "__main__":
    main()
