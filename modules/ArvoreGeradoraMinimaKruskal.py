from modules.Grafo1 import Grafo


# utiliando algoritmo de Kruskal
def arvore_geradora_minima(grafo):
    A = []

    S = []
    arestas = []
    for vertice in grafo.grafo:
        # fazer lista de arestas
        for aresta in vertice.edgesSaida:
            arestas.append(aresta)

        # fazer estrutura de dados S
        S.append([int(vertice.id)])

    # ordenar as arestas por peso
    arestas.sort(key=lambda x: x.peso, reverse=False)

    # loop principal do algoritmo, rodando todas as arestas ordenadas por peso
    for aresta in arestas:
        # garantia de aresta segura
        if S[aresta.a - 1] != S[aresta.b - 1]:
            A.append(aresta)

            # soma das arestas
            x = S[aresta.a - 1] + S[aresta.b - 1]

            for y in x:
                S[y - 1] = x

    # pegar a soma de pesos da árvore
    soma_peso_arvore = 0
    for aresta in A:
        soma_peso_arvore += aresta.peso

    # printtar no formato do exercício
    print(soma_peso_arvore)

    string = ""
    for aresta in A:
        string += f'{aresta.a + 1}-{aresta.b + 1}, '
    print(string[:-2])


def main():
    grafo = Grafo()
    grafo.ler("../testes/arvore_geradora_minima/agm_tiny.net")
    arvore_geradora_minima(grafo)


if __name__ == "__main__":
    main()
