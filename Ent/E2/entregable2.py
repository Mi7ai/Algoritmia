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


def lista_vecinos(g: UndirectedGraph):
    V = g.V
    lista_vertices = []
    for v in V:
        vecinos = int (len(g.succs(v)))
        x = (v[0])
        y = (v[1])
        lista_vertices.append((vecinos, x, y))
    return sorted(lista_vertices, key=lambda i:(-i[0],-i[1],-i[2]))


# devuelve una lista decreciente ordenada por longitud de vecinos de los vertices, coordenada x, coordenada y


def lista_vecinos2(g: UndirectedGraph):
    # s1 = sorted(g.V, key=lambda i: (-len(g.succs(i))))   # orden por la longitud de vecinos de los vertices decreciente
    # s2 = sorted(g.V, key=lambda i: -i[0])  # orden por la coordenada x de los vertices decreciente
    # s3 = sorted(g.V, key=lambda i: -i[1])  # orden por la coordenada y de los vertices decreciente

    # print("s1:", s1)
    # print("s2:", s2)
    # print("s3:", s3)

    # ordenacion decrediente porlongitud de los vecinos de los vertice,
    # luego por valor de coordenada x
    # luego por valor de coordenada y
    s = sorted(g.V, key=lambda i: (-len(g.succs(i)), -i[0], -i[1]))
    # print("s:", s)
    return list(s)

# muestra todos los vertices con su nr de vecinos


def vecinosV(g: UndirectedGraph):
    for e in g.V:
        print("Vertice: {}, nr vecinos = {}".format(e, len(g.succs(e))))


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


def algoritmo1(g: UndirectedGraph) -> Tuple[int, Dict[Tuple[int,int],int]]:
    lista = lista_vecinos2(g)
    vertices_ordenados = []
    for i in lista:
        vertices_ordenados.append((i[0], i[1]))
    lista_colores = colorea(UndirectedGraph(V=vertices_ordenados, E=g.E))
    n_colores = 0
    color_dic = {}
    for conjunto in lista_colores:
        for gr in conjunto:
            color_dic[gr] = n_colores
        n_colores += 1
    return len(lista_colores),color_dic #cantidad colores y diccionario de colores


def algoritmo2(g: UndirectedGraph) -> Tuple[int, Dict[Tuple[int, int], int]]:
    pass
    # TODO



if __name__ == '__main__':
    parametros = len(sys.argv)
    datos = aristas(filename)
    g = UndirectedGraph(E=datos)

    # vecinosV(g) # muestra el nr de vecinos de cada vertice

    if parametros == 3 and sys.argv[2] == "-1":
        # usamos el algoritmo1
        tup = algoritmo1(g)
        cant_color = tup[0]
        dic = tup[1]

        print(cant_color)
        for t, c in dic.items():
            print(t[0], t[1], c)

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

