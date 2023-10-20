import sys

from modules.Grafo import Grafo


# usando algoritmo de Floyd-Warshall
def caminhos_grafo(grafo):
    # criar matriz de adjacência
    matriz0 = []
    for i in range(len(grafo.grafo)):
        linha = []
        for j in range(len(grafo.grafo)):
            if i == j:
                linha.append(0)
            elif i != j and grafo.haAresta(i + 1, j + 1):
                linha.append(grafo.peso(i + 1, j + 1))
            elif i != j and not grafo.haAresta(i + 1, j + 1):
                linha.append(sys.float_info.max)
        matriz0.append(linha)

    # atualizar matriz de adjacência
    for k in range(grafo.qtdVertices()):
        for u in range(grafo.qtdVertices()):
            for v in range(grafo.qtdVertices()):
                matriz0[u][v] = min(matriz0[u][v], (matriz0[u][k] + matriz0[k][v]))

    # printtar no formato do exercício
    for i in range(grafo.qtdVertices()):
        print(f'{i + 1}:', end="")
        for j in range(grafo.qtdVertices()):
            if j == grafo.qtdVertices() - 1:
                print(matriz0[i][j])
            else:
                print(matriz0[i][j], end=",")


def main():
    grafo = Grafo()
    grafo.ler("../testes/caminho_minimo/fln_pequena.net")
    caminhos_grafo(grafo)


if __name__ == "__main__":
    main()
