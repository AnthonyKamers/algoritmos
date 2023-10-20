from modules.Grafo import Grafo


# https://stackabuse.com/python-how-to-flatten-list-of-lists/
def flatten(list_of_lists):
    if len(list_of_lists) == 0:
        return list_of_lists
    if isinstance(list_of_lists[0], list):
        return flatten(list_of_lists[0]) + flatten(list_of_lists[1:])
    return list_of_lists[:1] + flatten(list_of_lists[1:])


class Aresta:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.hasPassed = False


def testeArestas(arestas, aux):
    return list(filter(lambda x: x.hasPassed == aux, arestas))


def criarArestas(grafo):
    arestas = []

    for node in grafo.grafo:
        for item in node.edgesSaida:
            aresta = Aresta(node.id, item[0] + 1)
            arestas.append(aresta)

    return arestas


def verificar_ciclo_euleriano(grafo):
    arestas = criarArestas(grafo)

    v = 1  # seleciona arbitrariamente vértice conectado a uma aresta

    (retorno, ciclo) = buscar_subciclo_euleriano(v, arestas)

    if retorno == False:
        print("0")
    else:
        if len(testeArestas(arestas, False)) != 0:
            print("0")
        else:
            print("1")
            print(*ciclo, sep=",")


def buscar_subciclo_euleriano(vertice, arestas):
    ciclo = []
    ciclo.append(int(vertice))
    vertice_alvo = vertice

    while True:
        aresta_save = None
        proximo = None
        for aresta in arestas:
            if int(aresta.a) == int(vertice) and not aresta.hasPassed:
                aresta_save = aresta
                proximo = aresta.b
                aresta.hasPassed = True
                break
            elif int(aresta.b) == int(vertice) and not aresta.hasPassed:
                aresta_save = aresta
                proximo = aresta.a
                aresta.hasPassed = True
                break

        if not aresta_save:
            return (False, None)
        else:
            vertice = proximo

            # adiciona vértice ao final do ciclo
            ciclo.append(int(vertice))

            # finalização do loop
            if int(vertice) == int(vertice_alvo):
                break

    # teste de arestas não visitadas
    # para cada aresta não visitada, fazer o loop
    while True:
        arestasFalsas = testeArestas(arestas, False)
        if len(arestasFalsas) == 0:
            break

        v1 = arestasFalsas[0].a
        (retorno, ciclo1) = buscar_subciclo_euleriano(v1, arestasFalsas)

        if not retorno:
            return (False, None)

        # substituir no ciclo original onde tem v1, substituir por ciclo
        for k, v2 in enumerate(ciclo):
            if int(v2) == int(v1):
                ciclo[k] = ciclo1
                break

        ciclo = flatten(ciclo)

    return (True, ciclo)


def main():
    grafo = Grafo()
    grafo.ler("../testes/ciclo_euleriano/ContemCicloEuleriano.net")
    verificar_ciclo_euleriano(grafo)


if __name__ == "__main__":
    main()
