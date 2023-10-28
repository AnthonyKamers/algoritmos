from modules.Grafo1 import Grafo


def find_vertice(grafo, id):
    for vertice in grafo.grafo:
        if int(vertice.id) == int(id):
            return vertice


def get_min_caminho(grafo, caminho):
    pesos = []
    for vertice in grafo.grafo:
        for arco in vertice.edgesSaida:
            for k, item in enumerate(caminho):
                if k != len(caminho) - 1:
                    if arco.a + 1 == caminho[k] and arco.b + 1 == caminho[k + 1]:
                        pesos.append(arco.peso)
                    if len(pesos) == len(caminho):
                        break
    print(caminho)
    print(min(pesos))


def edmonds_karp(grafo, vertice_fonte, vertice_sorvedouro):
    # Configurando todos os vertices
    visitados = [False] * grafo.qtdVertices()
    antecessores = [None] * grafo.qtdVertices()

    # Configurando vertice de origem
    visitados[vertice_fonte - 1] = True

    # Preparando fila de visitas
    fila_de_visitas = []

    # Iniciando busca pela fonte
    vertice_fonte1 = find_vertice(grafo, vertice_fonte)
    fila_de_visitas.append(vertice_fonte1)

    # Propagação das visitas
    while fila_de_visitas != []:
        u = fila_de_visitas.pop()

        # arco.a = u | arco.b = v
        for arco in u.edgesSaida:
            if visitados[arco.b] == False and arco.peso > 0:
                visitados[arco.b] = True
                antecessores[arco.b] = int(u.id)

                # Sorvedouro encontrado. Criar caminho aumentante
                if (arco.b + 1) == vertice_sorvedouro:
                    caminho = [vertice_sorvedouro]
                    vertice_auxiliar = vertice_sorvedouro

                    while vertice_auxiliar != vertice_fonte:
                        vertice_auxiliar = antecessores[vertice_auxiliar - 1]
                        caminho.insert(0, vertice_auxiliar)

                    get_min_caminho(grafo, caminho)

                fila_de_visitas.append(find_vertice(grafo, arco.b + 1))
    return None


def main():
    grafo = Grafo()
    grafo.ler("../testes/fluxo_maximo/wiki.net")
    edmonds_karp(grafo, 1, 7)


if __name__ == "__main__":
    main()
