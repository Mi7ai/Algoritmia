from algoritmia.datastructures.mergefindsets import MergeFindSet
from algoritmia.datastructures.digraphs import UndirectedGraph
from Lab.labyrinthviewer import LabyrinthViewer
from algoritmia.datastructures.queues import Fifo

from random import shuffle


def create_labyrinth(rows, cols, n=0):
    # general expressions of all vertexes
    vertices = [(row, col) for row in range(rows) for col in range(cols)]

    mfs = MergeFindSet()
    edges = []

    for v in vertices:
        # print(v)
        mfs.add(v)

    # add the bottom row and right column to edge list and shuffle it
    for row, col in vertices:
        if row + 1 < rows:
            edges.append([(row, col), (row + 1, col)])
        if col + 1 < cols:
            edges.append([(row, col), (row, col + 1)])
    shuffle(edges)
    # # #
    # for i in edges:
    #     a, b = i
    #     print(a, b)
    ###

    corridors = []

    i = 0
    # if the edges are not in the same set, merge them in the same one and add them to corridors
    for u, v in edges:
        if mfs.find(u) != mfs.find(v):
            mfs.merge(u, v)
            corridors.append((u, v))
        elif i < n:
            corridors.append((u, v))
            i += 1

    # for u, v in corridors:
    #     print("Path: {} -> {}".format(u, v))
    # print(len(corridors))

    return UndirectedGraph(E=corridors)


def recuperador_camino(lista_aristas, v):
    bp = {}
    for orig, dest in lista_aristas:
        bp[dest] = orig

    # reconstruir camino hacia atras
    camino = []
    camino.append(v)

    while v != bp[v]:
        v = bp[v]
        camino.append(v)

    camino.reverse()
    return camino


def recorredor_aristas_anchura(lab, v_inicio):
    def recorrer_desde(u, v):
        q.push((u, v))
        seen.add(v)

        # recorrer la cola, sacar el 1 valor
        # añadir a la lista de aristas
        # mirar sus vecinos para añadirlos tambien

        while len(q) > 0:
            u, v = q.pop()
            aristas.append((u, v))
            for suc in lab.succs(v):
                if suc not in seen:
                    seen.add(suc)
                    q.push((v, suc))
        return aristas

    aristas = []
    q = Fifo()
    seen = set()
    return recorrer_desde(v_inicio, v_inicio)

def recorredor_aristas_profundidad(lab, v_inicio):
    def recorrer_desde(u, v):

        # recorrer la cola, sacar el 1 valor
        # añadir a la lista de aristas
        # mirar sus vecinos para añadirlos tambien
        seen.add(v)
        aristas.append((u, v))
        for suc in lab.succs(v):
            if suc not in seen:
                recorrer_desde(v, suc)

    aristas = []
    seen = set()
    recorrer_desde(v_inicio, v_inicio)
    return aristas


def path(g, source, target):
    aristas = recorredor_aristas_profundidad(g, source)
    camino = recuperador_camino(aristas, target)

    return camino


def shortest_path(g, source, target):
    aristas = recorredor_aristas_anchura(g, source)
    camino = recuperador_camino(aristas, target)

    return camino


if __name__ == '__main__':
    rows = 30
    cols = 40

    lab = create_labyrinth(rows, cols, 30)
    lv = LabyrinthViewer(lab, canvas_width=600, canvas_height=400, margin=10)

    v_inicio = (0, 0)
    v_tesoro = (rows-1, cols-1)

    path1 = shortest_path(lab, v_inicio, v_tesoro)
    path2 = path(lab, v_inicio, v_tesoro) # en profundidad


    lv.add_path(path1, 'blue')
    lv.add_path(path2, 'red', offset=4)
    lv.run()
