from modules.CaminhoMinimoDijkstra import dijkstra, calcular_inicio_fim
from modules.Grafo1 import Grafo


def pedagio_dijkstra(grafo, p, s, t, preco_combustivel, media_veiculo):
    def create_grafo_custo():
        vertices = []
        for vertice in grafo.grafo:
            vertices.append((vertice.id, vertice.rotulo))

        arcos = []
        for arco in grafo.arcos:
            custo_gasolina = (arco.peso / media_veiculo) * preco_combustivel
            custo_total = custo_gasolina + p[arco.a + 1] + p[arco.b + 1]
            arcos.append((arco.a + 1, arco.b + 1, custo_total))

        grafo_return = Grafo()
        grafo_return.argumentos(vertices, arcos)
        return grafo_return

    grafo_custo = create_grafo_custo()
    custo, antecessor = dijkstra(grafo_custo, s)
    calcular_inicio_fim(grafo_custo, custo, antecessor, t)


def main():
    grafo = Grafo()
    grafo.argumentos(
        [(1, "A"), (2, "B"), (3, "C"), (4, "D"), (5, "E")],
        [
            (1, 2, 100),
            (2, 3, 200),
            (2, 4, 200),
            (3, 5, 150),
            (4, 5, 400),
            (5, 1, 750)
        ])

    # mapeamento preço pedágio
    p = {
        1: 10,
        2: 10,
        3: 2.50,
        4: 100,
        5: 35
    }

    s = 1  # início
    t = 5  # destino
    preco_litro = 5.80
    km_litro = 10

    pedagio_dijkstra(grafo, p, s, t, preco_litro, km_litro)


if __name__ == "__main__":
    main()
