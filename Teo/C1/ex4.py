from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet
from random import shuffle
from algoritmia.datastructures.queues import Fifo

__author__ = "Mihai"
__status__ = "Finished"




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


# LISTA DE ARISTAS EN ANCHURA

# devolver una lista de aristas con las aristas que hemos utilizado para hacer el recorrido de vértices
def recorredor_aristas_anchura(lab, v_inicio):
	def recorrer_desde(u, v):
		q.push((u, v))
		seen.add(v)

		# recorrer la cola, sacar la 1 arista
		# añadirla a la lista de aristas
		# mirar sus vecinos para añadir las siguientes

		while len(q) > 0:
			u, v = q.pop()
			aristas.append((u, v))
			for suc in lab.succs(v):
				if suc not in seen:
					seen.add(suc)
					q.push((v, suc))

	aristas = []
	q = Fifo()
	seen = set()
	recorrer_desde(v_inicio, v_inicio)
	return aristas

# LISTA DE ARISTAS EN PROFUNDIDAD

def recorredor_aristas_profundidad(lab, v_inicio):
	def recorrer_desde(u, v):

		# añadir a la lista de aristas
		# mirar sus vecinos para las añadir siguientes

		seen.add(v)
		aristas.append((u, v))
		for suc in lab.succs(v):
			if suc not in seen:
				recorrer_desde(v, suc)

	aristas = []
	seen = set()
	recorrer_desde(v_inicio, v_inicio)
	return aristas

if __name__ == '__main__':
	rows, cols = 2, 2
	lab = create_labyrinth(rows, cols)
	# LabyrinthViewer(lab, canvas_width=600, canvas_height=400, margin=10).run()
	v_inicio = (0, 0)

	lista_aristas = recorredor_aristas_anchura(lab, v_inicio)
	lista_aristas = recorredor_aristas_profundidad(lab, v_inicio)

	for a in lista_aristas:
		print(a)
