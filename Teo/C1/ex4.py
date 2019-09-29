from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet
from random import shuffle
from Lab.labyrinthviewer import LabyrinthViewer
from algoritmia.datastructures.queues import Fifo

__author__ = "Mihai"
__status__ = "Finished"

# LISTA DE ARISTAS EN ANCHURA


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


# devolver una lista de aristas con las aristas que hemos utilizado
# para hacer el recorrido de vértices
def recorredor_vertices_anchura(lab, v_inicio):
	def recorrer_desde(u, v):
		q.push((u, v))
		seen.add(v)

		# recorrer la cola, sacar el 1 valor
		# añadirl a la lista de aristas
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


if __name__ == '__main__':
	lab = create_labyrinth(2, 2)
	# LabyrinthViewer(lab, canvas_width=600, canvas_height=400, margin=10).run()
	v_inicio = (0, 0)

	aristas = recorredor_vertices_anchura(lab, v_inicio)

	for a in aristas:
		print(a)
