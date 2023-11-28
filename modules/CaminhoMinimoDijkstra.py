import sys

from modules.Grafo1 import Grafo


def calcular_inicio_fim(grafo, distancia, antecessor, destino):
    destino_index = destino - 1

    if distancia[destino_index] is None:
        print("Não há rota para esse destino")
        return

    vertice_now = antecessor[destino_index]
    caminho = [vertice_now, grafo.grafo[destino_index]]
    while True:
        vertice_now = antecessor[vertice_now.id - 1]
        if vertice_now is None:
            break
        caminho.insert(0, vertice_now)

    rotulos = [x.rotulo for x in caminho]

    print(f'Custo total: R${distancia[destino_index]}')
    print('Caminho: <', end="")
    print(*rotulos, sep=",", end="")
    print(">")


def dijkstra(grafo, vertice_origem):
    qtd_vertices = len(grafo.grafo)
    distancia = [sys.float_info.max for x in range(qtd_vertices)]
    antecessor = [None for x in range(qtd_vertices)]
    custo = [False for x in range(qtd_vertices)]

    distancia[vertice_origem - 1] = 0

    while False in custo:
        u = list(filter(lambda x: distancia[x.id - 1] == sys.float_info.max or custo[x.id - 1] is False, grafo.grafo))[0]
        distancia_u = distancia[u.id - 1]
        custo[u.id - 1] = True

        for vizinho in u.vizinhos():
            v = grafo.grafo[vizinho - 1]

            distancia_v = distancia[v.id - 1]
            peso_u_v = grafo.peso(u.id, v.id)
            if distancia_v > distancia_u + peso_u_v:
                distancia[v.id - 1] = distancia_u + peso_u_v
                antecessor[v.id - 1] = u

    return distancia, antecessor


if __name__ == "__main__":
    grafo_now = Grafo()
    grafo_now.ler("../testes/caminho_minimo/fln_pequena.net")
    print(dijkstra(grafo_now, 1))
