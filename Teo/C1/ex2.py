from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet
from random import shuffle
from Lab.labyrinthviewer import LabyrinthViewer
from algoritmia.datastructures.queues import Fifo

__author__ = "Mihai"
__status__ = "Finished"


# BUSCAR TESORO EN PROFUNDIDAD RECURSIVO


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


# Busca el tesoro y devuelve una tupla (x, y), o None si no lo encuentra
def busca_tesoro_primero_profundidad(lab, v_inicio):
	def explorar_desde(v):
		seen.add(v)

		# v es v_inicio
		# ver si es el tesoro
		# si no, mirar sus vecinos recursivamente

		if v == v_tesoro:
			return v  # he encontrado el tesoro
		for suc in lab.succs(v):
			if suc not in seen:
				res = explorar_desde(suc)
				if res is not None:
					return res

	seen = set()
	return explorar_desde(v_inicio)


if __name__ == '__main__':
	rows, cols = 20, 25
	lab = create_labyrinth(rows, cols)
	# LabyrinthViewer(lab, canvas_width=600, canvas_height=400, margin=10).run()

	v_inicio = (0, 0)
	v_tesoro = (2, 3)

	pos_tesoro_encontrada = busca_tesoro_primero_profundidad(lab, v_inicio)

	if pos_tesoro_encontrada == None:
		print("Tesoro no encontrado")
	else:
		print("Tesoro encontrado en la habitación {0}".format(pos_tesoro_encontrada))
