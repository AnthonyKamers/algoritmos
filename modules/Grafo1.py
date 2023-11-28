import sys


class Arco:
    def __init__(self, a, b, peso):
        self.a = a
        self.b = b
        self.peso = peso


class Vertice:
    def __init__(self, id, rotulo):
        self.id = id
        self.rotulo = rotulo
        self.edgesEntrada = []
        self.edgesSaida = []

    def edgeEntrada(self, arco):
        self.edgesEntrada.append(arco)

    def edgeSaida(self, arco):
        self.edgesSaida.append(arco)

    def grau(self):
        return len(self.edgesSaida) + len(self.edgesEntrada)

    def vizinhosSaida(self):
        return [arco.b for arco in self.edgesSaida]

    def vizinhosEntrada(self):
        return [arco.a for arco in self.edgesEntrada]

    def vizinhos(self):
        vizinhos = []
        for aresta in self.edgesSaida:
            vizinhos.append(aresta.b + 1)
        for aresta in self.edgesSaida:
            vizinhos.append(aresta.a + 1)
        return vizinhos

    def haAresta(self, v):
        for aresta in self.edgesEntrada + self.edgesSaida:
            if aresta.a == (v - 1) or aresta.b == (v - 1):
                return True
        return False

    def peso(self, v):
        for aresta in self.edgesSaida + self.edgesEntrada:
            if aresta.a == (v - 1) or aresta.b == (v - 1):
                return aresta.peso
        return sys.float_info.max


class Grafo:
    def __init__(self):
        self.grafo = []
        self.arcos = []

    def argumentos(self, vertices, arestas):
        for id, rotulo in vertices:
            self.grafo.append(Vertice(id, rotulo))

        for aresta in arestas:
            u, v, peso = aresta
            arco = Arco(u - 1, v - 1, peso)
            self.grafo[u - 1].edgeSaida(arco)
            self.grafo[v - 1].edgeEntrada(arco)
            self.arcos.append(arco)

    def ler(self, arquivo):
        file = open(arquivo, 'r')

        first = True
        reading = False
        edges = False
        qtd = 0
        for line in file:
            line = line[0:-1]  # retirar \n das linhas
            aux = line

            if edges:
                aux = aux.split(" ")
                arco = Arco(int(aux[0]) - 1, int(aux[1]) - 1, float(aux[2]))

                self.grafo[int(aux[0]) - 1].edgeSaida(arco)
                self.grafo[int(aux[1]) - 1].edgeEntrada(arco)
                self.arcos.append(arco)

            if aux == "*edges" or aux == "*arcs":
                reading = False
                edges = True

            if reading:
                split = aux.split('"') if aux.find('"') > 0 else aux.split(' ')
                id = int(split[0])
                rotulo = split[1]
                self.grafo.append(Vertice(id, rotulo))

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

    def vizinhosSaida(self, index):
        return self.grafo[index - 1].vizinhosSaida()

    def haAresta(self, u, v):
        return self.grafo[u - 1].haAresta(v)

    def peso(self, u, v):
        return self.grafo[u - 1].peso(v)
