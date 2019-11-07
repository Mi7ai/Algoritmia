import sys
from typing import Tuple, Dict
from algoritmia.datastructures.prioritymaps import MaxHeapMap
from algoritmia.datastructures.digraphs import UndirectedGraph
from Utils.graphcoloring2dviewer import GraphColoring2DViewer

filename = sys.argv[1]


def aristas (filename):
    datos = []
    try:
        f = open(filename, "r")

        for line in f:
            x1, y1, x2, y2 = line.split(" ")
            vertice1 = (int(x1), int(y1))
            vertice2 = (int(x2), int(y2))
            arista = (vertice1, vertice2)

            datos.append(arista)

        f.close()
    except IOError:
        print("File cannot be open!")

    return datos


# muestra todos los vertices con su nr de vecinos


def vecinosV(g: UndirectedGraph):
    for e in g.V:
        print("Vertice: {}, nr vecinos = {}".format(e, len(g.succs(e))))


def algoritmo1(g: UndirectedGraph) -> Tuple[int, Dict[Tuple[int, int], int]]:
    vertices_ordenados = sorted(g.V, key=lambda i: (-len(g.succs(i)), -i[0], -i[1]))

    n_colores = 0
    color_dic = {}

    for v in vertices_ordenados:
        color = 0
        colorvecinos = [color_dic.get(vecino) for vecino in g.succs(v)]

        # cuenta cuantos color tienen los vecinos
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
    maxHeap = MaxHeapMap()

    for v in g.V:
        maxHeap[v] = (0, len(g.succs(v)), v[0], v[1])

    while len(maxHeap) > 0:
        v_actual = maxHeap.extract_opt()
        colores = [ color_dic.get(vecino) for vecino in g.succs(v_actual)]

        c = 0
        while True:
            if c not in colores:
                color_dic[v_actual] = c
                for vecino in g.succs(v_actual):
                    if vecino in maxHeap:
                        maxHeap[vecino] = (maxHeap[vecino][0]+1, maxHeap[vecino][1], maxHeap[vecino][2], maxHeap[vecino][3])
                break
            c += 1

            if c > n_colores:
                n_colores = c

    return n_colores+1, color_dic

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

    if parametros == 3 and sys.argv[2] == "-1":
        # usamos el algoritmo1
        cant_color, dic_vertices_colores = algoritmo1(g)

        print(cant_color)
        for elem in ordenacion_final(dic_vertices_colores):
            print(elem[0], elem[1], elem[2])

    elif parametros == 3 and sys.argv[2] == "-2":
        # usamos el algoritmo2
        cant_color, dic_vertices_colores = algoritmo2(g)

        print(cant_color)
        for elem in ordenacion_final(dic_vertices_colores):
            print(elem[0], elem[1], elem[2])

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
