import sys

from modules.Grafo import Grafo


class VerticeDFS:
    def __init__(self, vertice):
        self.vertice = vertice
        self.hasPassed = False
        self.tempo = sys.float_info.max
        self.final = sys.float_info.max
        self.antecessor = None

    def show(self):
        antecessor = self.antecessor.vertice.rotulo if self.antecessor is not None else ""
        print(self.vertice.rotulo, self.tempo, self.final, antecessor)


def get_path_root(vertice_pai, filhos):
    vertice_backup = vertice_pai
    vertice_now = vertice_pai
    caminho = []

    rodando = True
    while rodando:
        for item in filhos:
            if item.antecessor == vertice_now:
                caminho.append(item)
                vertice_now = item
                break
        if vertice_now != vertice_backup:
            vertice_backup = vertice_now
            continue
        break

    caminho.insert(0, vertice_pai)

    # printtar no formato do exercício
    saida = ""
    for item in caminho:
        saida += str(item.vertice.id) + ","

    print(saida[:-1])


def componentes_fort_conexas(grafo):
    vertices = DFS(grafo)
    vertices.sort(key=lambda x: x.final, reverse=True)  # saber ordem do tempo final, para passar na próxima etapa

    vertices_final = DFS(grafo, vertices1=vertices)

    roots = list(filter(lambda x: x.antecessor == None, vertices_final))
    filhos = list(filter(lambda x: x.antecessor != None, vertices_final))

    # chamar para cada raiz, para fazer o caminho de cada uma (printtar no formato do exercício)
    for i in roots:
        get_path_root(i, filhos)


def DFS(grafo, vertices1=None):
    vertices = criar_verticesDFS(grafo)

    tempo = 0  # tempo de início
    for i in range(0, len(vertices)):
        id_now = i if not vertices1 else int(vertices1[i].vertice.id) - 1

        if vertices[id_now].hasPassed == False:
            vertices, tempo = DFS_visit(vertices[id_now], vertices, tempo, entrada=False if not vertices1 else True)

    return vertices


def DFS_visit(verticeOrigem, vertices, tempo, entrada=False):
    indexVerticeOrigem = int(verticeOrigem.vertice.id) - 1

    vertices[indexVerticeOrigem].hasPassed = True
    tempo += 1
    vertices[indexVerticeOrigem].tempo = tempo

    vizinhos = verticeOrigem.vertice.vizinhosSaida() if not entrada else verticeOrigem.vertice.vizinhosEntrada()

    for id in vizinhos:
        if vertices[id].hasPassed == False:
            vertices[id].antecessor = verticeOrigem
            vertices, tempo = DFS_visit(vertices[id], vertices, tempo, entrada=entrada)

    tempo += 1
    vertices[indexVerticeOrigem].final = tempo

    return vertices, tempo


def criar_verticesDFS(grafo):
    return [VerticeDFS(vertice) for vertice in grafo.grafo]


def main():
    grafo = Grafo()
    grafo.ler("../testes/dirigidos/teste2.net")
    componentes_fort_conexas(grafo)


if __name__ == "__main__":
    main()
