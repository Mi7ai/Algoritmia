from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet
from random import shuffle
from Lab.labyrinthviewer import LabyrinthViewer
from algoritmia.datastructures.queues import Fifo

__author__ = "Mihai"
__status__ = "Finished"

# primero en anchura. Algoritmo no recursivo + cola FIFO


def create_labyrinth(rows, cols):
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

	# if the edges are not in the same set, merge them in the same one and add them to corridors
	for u, v in edges:
		if mfs.find(u) != mfs.find(v):
			mfs.merge(u, v)
			corridors.append((u, v))

	# for u, v in corridors:
	# 	print("Path: {} -> {}".format(u, v))
	return UndirectedGraph(E=corridors)


def busca_tesoro_primero_anchura(lab, v_inicio):
	# creamos cola y set
	q = Fifo()
	seen = set()

	# añadimos el valor inicial en la cola y el set
	q.push(v_inicio)
	seen.add(v_inicio)

	# recorrer la cola, sacar el 1 valor
	# ver si es el tesoro
	# si no, mirar sus vecinos

	while len(q) > 0:
		v = q.pop()
		print("Pop: {}.....Tesoro: {}".format(v, v_tesoro))
		if v == v_tesoro:
			return v  # he encontrado el tesoro
		for suc in lab.succs(v):
			print("Suc de v: {}".format(suc))
			if suc not in seen:
				seen.add(suc)
				q.push(suc)
	return None


if __name__ == '__main__':
	lab = create_labyrinth(20, 25)
	# LabyrinthViewer(lab, canvas_width=600, canvas_height=400, margin=10).run()

	v_inicio = (0, 0)
	v_tesoro = (2, 3)

	pos_tesoro_encontrada = busca_tesoro_primero_anchura(lab, v_inicio)

	if pos_tesoro_encontrada == None:
		print("Tesoro no encontrado")
	else:
		print("Tesoro encontrado en la habitación {0}".format(pos_tesoro_encontrada))