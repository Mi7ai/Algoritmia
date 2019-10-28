from Utils.graphcoloring2dviewer import GraphColoring2DViewer
from algoritmia.datastructures.digraphs import UndirectedGraph
from typing import Tuple, Dict
import sys

__author__ = "Mihai Manea"
__status__ = "Pending"

filename = sys.argv[1]

vertices = []


def load_aristas (filename):
    datos = []

    try:
        f = open(filename, "r")

        for line in f:
            x1, y1, x2, y2 = line.split(" ")
            vertice1 = (int(x1), int(y1))
            vertice2 = (int(x2), int(y2))
            arista = (vertice1, vertice2)

            vertices.append(vertice1)
            vertices.append(vertice2)

            datos.append(arista)
        f.close()
    except IOError:
        print("File cannot be open!")

    return datos


def colorea(g: UndirectedGraph):
    V = set(g.V)

    res = []
    while len(V) > 0:
        grupo = set()
        for v in V:
            if all(v not in g.succs(u) for u in grupo):
                grupo.add(v)
        V -= grupo
        res.append(grupo)
    return res


def algoritmo1(g: UndirectedGraph):

    indices_ordenados = sorted(range(len(g.V)), key=lambda i: len(g.V.succs(i)))

    return indices_ordenados



# def algoritmo2(g: UndirectedGraph) -> Tuple[int, Dict[Tuple[int, int], int]]:




if __name__ == '__main__':
    parametros = len(sys.argv)
    datos = load_aristas(filename)
    g = UndirectedGraph(E=datos)

    if parametros == 3 and sys.argv[2] == "-1":
         # usamos el algoritmo1
        a1 = algoritmo1(g) # lista con indices ordenadodos por la longitud de los vecinos del vertice
        for v in a1:
            print(vertices[v])

    elif parametros == 3 and sys.argv[2] == "-2":
        # usamos el algoritmo1
        pass
    elif parametros == 4 and sys.argv[3] == "-g":

        g = UndirectedGraph(E = [((-3,-2),(0,0)),((0,0),(1,1))])
        color_dic = {(-3,-2):0,(0,0):1,(1,1):2}#ponemos los colores
        viewer = GraphColoring2DViewer(g, color_dic, window_size=(800, 800))
        viewer.run()
        print(algoritmo1(g))
        print(colorea(g))
