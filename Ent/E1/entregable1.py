from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.mergefindsets import MergeFindSet
from algoritmia.datastructures.queues import Fifo
from Utils.labyrinthviewer import LabyrinthViewer
import sys

__author__ = "Mihai Manea"
__status__ = "Finished"

filename = sys.argv[1]

paredes = []  # paredes del laberinto


def load_labyrinth(filename):
	data = []
	try:
		f = open(filename, "r")

		tesorox, tesoroy = f.readline().split(" ")
		tesoro = (int(tesorox), int(tesoroy))

		bombax, bombay = f.readline().split(" ")
		bomba = (int(bombax), int(bombay))

		rows, cols = f.readline().split(" ")

		for line in f:
			data.append(line.split(","))
		f.close()
	except IOError:
		print("File cannot be open!")

	aristas = []

	col = 0
	for row in range(int(rows)):
		for pared in data[row]:
			if "s" not in pared and row + 1 < len(data):
				aristas.append(((row, col), (row + 1, col)))
			elif "s" in pared and row + 1 < len(data):
				paredes.append(((row, col), (row + 1, col)))
			if "e" not in pared and col + 1 < len(data[row]):
				aristas.append(((row, col), (row, col + 1)))
			elif "e" in pared and col + 1 < len(data[row]):
				paredes.append(((row, col), (row, col + 1)))
			col += 1
		col = 0
	# aristas.append(((0,1),(0,2)))
	return bomba, tesoro, int(rows), int(cols), UndirectedGraph(E=aristas)


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


# dado un vertice, calcula la distancia de todas las celdas a v_inicio
# devuelve un diccionario con:  --> clave: vertice
#                               ---> valor: distancia hasta v_inicio


def recorredor_aristas_anchura_distancias(lab, v_inicio):
	def recorrer_desde(u, v):
		q.push((u, v))
		seen.add(v)

		d[v_inicio] = 0  # el vertice que se pasa, su distancia es cero
		# print(v_inicio)
		# print(d[v_inicio])

		while len(q) > 0:
			u, v = q.pop()
			if u != v:  # si el sucesor de u es diferente
				d[v] = d[u] + 1  # sumo 1 a la distancia desde v a u

			for suc in lab.succs(v):
				if suc not in seen:
					seen.add(suc)
					q.push((v, suc))

	d = {}
	q = Fifo()
	seen = set()
	recorrer_desde(v_inicio, v_inicio)

	return d


# dados 2 diccionarios con las distancias desde la bomba y tresoro a todas las demas celdas
# dado 1 diccionario de paredes con forma de aristas
# encuentra la celda(en forma de arista) a romper


def celda(distancias_bomba_celdas, distancias_tesoro_celdas, paredes):
	u, v = paredes[0]
	a = distancias_bomba_celdas[u]
	b = distancias_bomba_celdas[v]

	c = distancias_tesoro_celdas[u]
	d = distancias_tesoro_celdas[v]

	minimo = min((a + d), (b + c)) + 1
	celdarom = paredes[0]

	for u, v in paredes:
		a = distancias_bomba_celdas[u]
		b = distancias_bomba_celdas[v]

		c = distancias_tesoro_celdas[u]
		d = distancias_tesoro_celdas[v]

		r = min((a + d), (b + c)) + 1
		if r < minimo:
			minimo = r
			celdarom = u, v

	return celdarom


def recuperador_camino(lista_aristas, v):
	bp = {}

	for orig, dest in lista_aristas:
		bp[dest] = orig
	# reconstruir camino hacia atras
	camino = [v]

	while v != bp[v]:
		v = bp[v]
		camino.append(v)

	camino.reverse()
	return camino


# devuelve el menor camino entre el source y el target


def shortest_path(g, source, target):
	aristas = recorredor_aristas_anchura(g, source)
	camino = recuperador_camino(aristas, target)

	return camino


# devuelve el menor camino entre el source y el target rompiendo un apared


def shortest_path_with_bomb(g, source, target, v_celda):
	aux = g
	aux._add_edge(v_celda)
	aristas = recorredor_aristas_anchura(g, source)
	camino = recuperador_camino(aristas, target)

	return camino


# muestra la longitud del camino sin bomba


def show_path(lab, v_inicio, v_tesoro):
	path1 = shortest_path(lab, v_inicio, v_tesoro)
	path2 = shortest_path(lab, v_tesoro, v_destino)

	return len(path1[1:]) + len(path2[1:])


# muestra la longitud del camino con bomba


def show_path_with_bomb(lab, v_inicio, v_tesoro, v_celda):
	path3 = shortest_path_with_bomb(lab, v_inicio, v_bomba, v_celda)
	path4 = shortest_path_with_bomb(lab, v_bomba, v_tesoro, v_celda)
	path5 = shortest_path_with_bomb(lab, v_tesoro, v_destino, v_celda)

	return len(path3[1:]) + len(path4[1:]) + len(path5[1:])


if __name__ == '__main__':
	v_bomba, v_tesoro, rows, cols, lab = load_labyrinth(filename)

	v_inicio = (0, 0)
	v_destino = (rows - 1, cols - 1)

	distancias_bomba_celdas = recorredor_aristas_anchura_distancias(lab, v_bomba)
	distancias_tesoro_celdas = recorredor_aristas_anchura_distancias(lab, v_tesoro)
	v_celda = celda(distancias_bomba_celdas, distancias_tesoro_celdas, paredes)

	if len(sys.argv) == 3 and sys.argv[2] == "-g":

		lv = LabyrinthViewer(lab, canvas_width=600, canvas_height=400, margin=10)

		print(v_celda)

		path1 = shortest_path(lab, v_inicio, v_tesoro)
		path2 = shortest_path(lab, v_tesoro, v_destino)

		print(len(path1[1:]) + len(path2[1:]))

		path3 = shortest_path_with_bomb(lab, v_inicio, v_bomba, v_celda)
		path4 = shortest_path_with_bomb(lab, v_bomba, v_tesoro, v_celda)
		path5 = shortest_path_with_bomb(lab, v_tesoro, v_destino, v_celda)

		print(len(path3[1:]) + len(path4[1:]) + len(path5[1:]))

		# azul es el inicio
		lv.add_marked_cell(v_inicio, "blue")
		# verde es el final
		lv.add_marked_cell(v_destino, "green")
		# amrillo es el tesoro
		lv.add_marked_cell(v_tesoro, "yellow")
		# rojo es la bomba
		lv.add_marked_cell(v_bomba, "red")
		# celda a romper
		lv.add_marked_cell(v_celda[0], "purple", fillCell=True)
		lv.add_marked_cell(v_celda[1], "purple", fillCell=True)

		lv.add_path(path1, 'blue')
		lv.add_path(path2, 'blue')

		lv.add_path(path3, 'green', offset=4)
		lv.add_path(path4, 'green', offset=4)
		lv.add_path(path5, 'green', offset=4)

		lv.run()
	else:
		print(v_celda)
		print(show_path(lab, v_inicio, v_tesoro))
		print(show_path_with_bomb(lab, v_inicio, v_tesoro, v_celda))
