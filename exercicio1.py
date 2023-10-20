from modules.Grafo import Grafo


def main():
    grafo = Grafo()
    grafo.argumentos([1, 2, 3, 4, 5, 6], [(1, 2), (3, 4), (5, 1)])


if __name__ == "__main__":
    main()
