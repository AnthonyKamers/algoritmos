from modules.Grafo import Grafo


# classe auxiliar para manter organizado
class NodeTree:
    def __init__(self, node):
        self.node = node
        self.nivel = 0
        self.pai = None


def print_tree(arvore, max_nivel):
    for i in range(0, max_nivel + 1):
        line = f'{i}: '
        for item in arvore:
            if item.nivel == i:
                aux = item.node.id[:-1]
                line += aux + ","
        print(line[:-1])


def busca_em_largura(grafo, n):
    # iniciar variaveis necessárias para realizar busca
    arvore = []
    passados = []
    fila = []
    max_nivel = 0

    node_init = NodeTree(grafo.grafo[n - 1])
    fila.append(node_init)

    # while da busca em largura
    while len(fila) != 0:
        u = fila.pop(0)

        arvore.append(u)
        passados.append(u.node.id)

        for vizinho in u.node.edgesSaida:
            if vizinho[0] not in passados:
                passados.append(vizinho[0])
                node_tree = NodeTree(grafo.grafo[vizinho[0]])
                node_tree.nivel = u.nivel + 1
                node_tree.pai = u
                fila.append(node_tree)
                max_nivel = u.nivel + 1

    print_tree(arvore, max_nivel)


def main():
    grafo = Grafo()
    grafo.ler("../testes/arvore_geradora_minima/agm_tiny.net")

    n = 1
    busca_em_largura(grafo, n)


if __name__ == "__main__":
    main()
