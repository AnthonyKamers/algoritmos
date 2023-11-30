from modules.BuscaLargura import busca_em_largura, find_path
from modules.Grafo import Grafo


def main():
    grafo = Grafo()

    vertices = [
        (1, "A"),
        (2, "B"),
        (3, "C"),
        (4, "D"),
        (5, "E"),
        (6, "F"),
    ]
    arestas = [
        (1, 2, 1),
        (2, 3, 1),
        (2, 4, 1),
        (2, 5, 1),
        (4, 5, 1),
        (5, 6, 1),
    ]

    grafo.argumentos(vertices, arestas)
    s = 1
    t = 5
    arvore, max_nivel = busca_em_largura(grafo, s)
    find_path(arvore, t)


if __name__ == "__main__":
    main()
