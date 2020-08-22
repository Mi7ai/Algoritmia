import sys
from algoritmia.datastructures.digraphs import Digraph, AdjacencyDigraph, WeightingFunction
from Utils.bt_scheme import BacktrackingSolver, BacktrackingOptSolver, PartialSolution, Solution, Iterable

filename = sys.argv[1]


def datos_fichero(filename):
	datos = []
	aristas = []
	aristas_pesos = {}
	try:
		f = open(filename, "r", encoding="utf-8")
		k = int(f.readline())
		v_ini = int(f.readline())
		nr_aristas = int(f.readline())

		for line in f:
			v_origen, v_destino, arista_peso = line.split(" ")
			arista = (int(v_origen), int(v_destino))
			# añadir aristas a la lista para crear el grafo
			aristas.append(arista)
			aristas_pesos[arista] = int(arista_peso)

		# datos.append([arista, int(arista_peso)])

		g = Digraph(E=aristas)
		d = WeightingFunction(aristas_pesos)

		f.close()
	except IOError:
		print("File cannot be open!")

	return k, v_ini, nr_aristas, g, d


def get_aristas(lista):
	res = []
	for arista in lista:
		v_origen = arista[0][0]
		v_destino = arista[0][1]
		res.append([v_origen, v_destino])

	return res


def camino_suave_solver(v_ini, g, d, k, total_aristas):
	class PartialPS(PartialSolution):
		def __init__(self, ds, ar: list, ultima_arista, contador):
			self.ds = ds
			self.n = len(ds)
			self.ar = ar
			self.ultima_arista = ultima_arista
			self.contador = contador

		def is_solution(self) -> bool:
			for polla in aristas_a_comprobar.items():
				arista = polla[0]
				valor = polla[1]
				if aristas_comprobadas[arista] != valor:
					return False
			return True

		def get_solution(self) -> Solution:
			return self.ds

		def successors(self) -> Iterable["PartialSolution"]:
			# if self.n  < len(g.E):
				for arista in self.ar:
					if self.n == 0:
						for v in g.succs(v_ini):
							arista_actual = (v_ini, v)
							ar2 = self.ar.copy()
							ar2.remove(arista_actual)
							aristas_comprobadas[arista_actual] = 1
							yield PartialPS(self.ds + (v_ini,) + (v,), ar2, arista_actual, self.contador+1)
					else:

						# comprobar si la ultima arista tiene camino con la arista actual
						if self.ultima_arista[1] == arista[0]:
							peso_arista_actual = d(arista)
							peso_arista_ultima = d(self.ultima_arista)
							# comprobamos que realmente sea un camino valido: <= k
							if abs(peso_arista_actual - peso_arista_ultima) <= k:
								ar2 = self.ar.copy()
								# ar2.remove(arista)

								arista_actual = (self.ultima_arista[1], arista[1])
								yield PartialPS(self.ds +(arista[1],), ar2, arista_actual, self.contador +1)

							else:
								# resetear aristas_comprobadas
								for arista in g.E:
									aristas_comprobadas[arista] = 0
								break
								# borrar el la arista en la cual estoy e irme a la arista anterior
								# ar2 = self.ar.copy()
								# ar2.remove(arista)
								# self.ar.remove(arista)
								# yield PartialPS(self.ds, ar2, self.ultima_arista, self.contador + 1)
						else:
							# no hay camino para esta arista, borramos la 1a arista de todas las aristas
							ar2 = self.ar.copy()
							ar2.remove(arista)
							aristas_comprobadas[arista] += 1
							# self.ar.remove(arista)
							# yield PartialPS(self.ds, ar2, self.ultima_arista, self.contador + 1)
							# self.contador += 1

	aristas_comprobadas = dict()
	aristas_a_comprobar = dict()
	for arista in g.E:
		aristas_comprobadas[arista] = 0

	for u,v in g.E:

		if g.in_degree(u) == 0:
			aristas_a_comprobar[(u, v)] = 1
		elif g.in_degree(u) > 0 and g.out_degree(u) > 0:
			# si le llegan aristas y tiene sucesor, le añado el valor de sucesor
			aristas_a_comprobar[(u, v)] = g.in_degree(u)

	initialPS = PartialPS((), list(g.E), (), 0)
	return BacktrackingSolver.solve(initialPS)


if __name__ == '__main__':
	k, v_ini, nr_aristas, g, d = datos_fichero(filename)
	# for a in g.E:
	# 	print(d(a))
	# print(g.E)
	# a = list(g.E)
	# a.append((1, 1))

	# print(nr_aristas)
	imprime = False
	for sol in camino_suave_solver(v_ini, g, d, k, nr_aristas):
		imprime = True
		print(sol)

	if not imprime:
		print("No hay solucion")

# for vo in g.V:
# 	for vd in g.succs(vo):
# 		print(d[vo, vd])
