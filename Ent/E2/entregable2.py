import sys
from typing import Tuple, Dict

from algoritmia.datastructures.digraphs import UndirectedGraph

from Utils.graphcoloring2dviewer import GraphColoring2DViewer

filename = sys.argv[1]
# vertices = []


def aristas (filename):
    datos = []
    try:
        f = open(filename, "r")

        for line in f:
            x1, y1, x2, y2 = line.split(" ")
            vertice1 = (int(x1), int(y1))
            vertice2 = (int(x2), int(y2))
            arista = (vertice1, vertice2)

            # vertices.append(vertice1)
            # vertices.append(vertice2)
            datos.append(arista)

        f.close()
    except IOError:
        print("File cannot be open!")

    return datos


# muestra todos los vertices con su nr de vecinos


def vecinosV(g: UndirectedGraph):
    for e in g.V:
        print("Vertice: {}, nr vecinos = {}".format(e, len(g.succs(e))))


def conjuntos():
    for i in colorea(g):
        print(i)


def colorea(G: UndirectedGraph):
    # crea copia de los vertices
    V = set(G.V)

    # lista con los grupos de vértices del mismo color
    res = []
    while len(V) > 0:
        # nuevo grupo vacío
        grupo = set()
        # añade los vértices cuyos sucesores no estén ya en grupo
        for v in V:
            if all(v not in G.succs(u) for u in grupo):
                grupo.add(v)
        # mantiene los elementos que estan en V pero no es grupo
        V -= grupo
        res.append(grupo)
    return res


def algoritmo1(g: UndirectedGraph) -> Tuple[int, Dict[Tuple[int, int], int]]:
    vertices_ordenados = sorted(g.V, key=lambda i: (-len(g.succs(i)), -i[0], -i[1]))

    n_colores = 0
    color_dic = {}

    for v in vertices_ordenados:
        color = 0
        colorvecinos = [color_dic.get(vecino) for vecino in g.succs(v)]

        # cuenta cuantos color tiene los vecinos
        while color in colorvecinos:
            if color is not None:
                color += 1

        # asigna el numero de colores totales - 1
        if color > n_colores:
            n_colores = color

        # asigna el menor color entre los colores de los vecinos
        color_dic[v] = color

    return n_colores+1, color_dic #cantidad colores y diccionario de colores


def algoritmo2(g: UndirectedGraph) -> Tuple[int, Dict[Tuple[int, int], int]]:
    color_dic = {}
    n_colores = 0

    for v in g.V:
        vecinos_coloreados = 0
        colorvecinos = [color_dic.get(vecino) for vecino in g.succs(v)]
        print(len(colorvecinos))
    vertices_ordenados = sorted(g.V, key=lambda i: (-len(g.succs(i)), -i[0], -i[1]))

    return n_colores, color_dic

# devuelve una lista ordenada por el valor de la coordenada x
# y en caso de empate ordenada por la coordenada y


def ordenacion_final(d: dict):
    temp_list = []
    for v, c in d.items():
        temp_list.append((v[0], v[1], c))

    return sorted(temp_list, key=lambda i: (i[0], i[1]))


if __name__ == '__main__':
    parametros = len(sys.argv)
    datos = aristas(filename)
    g = UndirectedGraph(E=datos)

    # vecinosV(g) # muestra el nr de vecinos de cada vertice
    # conjuntos()
    if parametros == 3 and sys.argv[2] == "-1":
        # usamos el algoritmo1
        cant_color, dic_vertices_colores = algoritmo1(g)

        print(cant_color)
        for elem in ordenacion_final(dic_vertices_colores):
            print(elem[0], elem[1], elem[2])

    elif parametros == 3 and sys.argv[2] == "-2":
        # usamos el algoritmo2
        # TODO
        pass
    elif parametros == 4 and sys.argv[3] == "-g":
        # usamor la opcion grafica
        op = sys.argv[2]  # que algoritmo usar (1 o 2)
        if op == "-1":
            tup = algoritmo1(g)
        else:
            tup = algoritmo2(g)
        cant_color = tup[0]
        dic = tup[1]

        viewer = GraphColoring2DViewer(g, dic, window_size=(800,800))
        viewer.run()
