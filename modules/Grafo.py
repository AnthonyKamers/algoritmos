import sys


class Node:
    def __init__(self, id, rotulo):
        self.id = id
        self.rotulo = rotulo
        self.edgesEntrada = []
        self.edgesSaida = []

    def edgeEntrada(self, id, valor):
        self.edgesEntrada.append([id, valor])

    def edgeSaida(self, id, valor):
        self.edgesSaida.append([id, valor])

    def grau(self):
        return len(self.edgesSaida) + len(self.edgesEntrada)

    def vizinhos(self):
        vizinhos = []
        for aresta in self.edgesSaida + self.edgesEntrada:
            vizinhos.append(aresta[0] + 1)
        return vizinhos

    def haAresta(self, v):
        for aresta in self.edgesSaida + self.edgesEntrada:
            if aresta[0] == (v - 1):
                return True
        return False

    def peso(self, v):
        for aresta in self.edgesSaida + self.edgesEntrada:
            if aresta[0] == (v - 1):
                return aresta[1]
        return sys.float_info.max


class Grafo:
    def __init__(self):
        self.grafo = []

    def argumentos(self, vertices, arestas):
        for vertice in vertices:
            self.grafo.append(Node(vertice, str(vertice)))

        for aresta in arestas:
            self.grafo[aresta[0] - 1].edgeSaida(aresta[1] - 1, 1)
            self.grafo[aresta[1] - 1].edgeEntrada(aresta[0] - 1, 1)

    def ler(self, arquivo):
        file = open(arquivo, 'r')

        first = True
        reading = False
        edges = False
        for line in file:
            line = line[0:-1]  # retirar \n das linhas
            aux = line

            if edges:
                aux = aux.split(" ")
                self.grafo[int(aux[0]) - 1].edgeSaida(int(aux[1]) - 1, float(aux[2]))
                self.grafo[int(aux[1]) - 1].edgeEntrada(int(aux[0]) - 1, float(aux[2]))

            if aux == "*edges":
                reading = False
                edges = True

            if reading:
                split = aux.split('"')
                id = split[0]
                rotulo = split[1]
                self.grafo.append(Node(id, rotulo))

            if first:
                qtd = int(aux.replace(aux[0:10], ""))
                reading = True
                first = False

    def qtdVertices(self):
        return len(self.grafo)

    def qtdArestas(self):
        qtd = 0
        for vertice in self.grafo:
            qtd += vertice.grau()

        return qtd

    def grau(self, index):
        return self.grafo[index - 1].grau()

    def rotulo(self, index):
        return self.grafo[index - 1].rotulo

    def vizinhos(self, index):
        return self.grafo[index - 1].vizinhos()

    def haAresta(self, u, v):
        return self.grafo[u - 1].haAresta(v)

    def peso(self, u, v):
        return self.grafo[u - 1].peso(v)


def main():
    grafo = Grafo()
    grafo.ler("../testes/arvore_geradora_minima/agm_tiny.net")


if __name__ == "__main__":
    main()
