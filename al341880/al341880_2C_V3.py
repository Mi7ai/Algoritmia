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

		g = AdjacencyDigraph(E=aristas)
		d = WeightingFunction(aristas_pesos)

		f.close()
	except IOError:
		print("File cannot be open!")

	return k, v_ini, nr_aristas, g, d

def cml(g,d, v_ini):
	vec = []
	vec = [-1]*len(g.V)
	vec[v_ini] = 0

	for vertice in g.V:
		for suc in g.succs(vertice):
			anterior_vertice = vec[vertice]
			if vec[suc] < vec[vertice]:

				vec[suc] = d(vertice,suc) + anterior_vertice

	return vec


def camino_suave_solver(v_ini, g, d, k, total_aristas):
	class PartialPS(PartialSolution):
		def __init__(self, ds: list, ar, v_ini):
			self.ds = ds
			self.n = len(ds)
			self.v_ini = v_ini
			self.ultima_ar = ar

		def is_solution(self) -> bool:
			if self.n > 0:

				if g.succs(self.ds[-1]) > 0:
					return False
				return True



		def get_solution(self) -> Solution:
			return self.ds

		def successors(self) -> Iterable["PartialSolution"]:
			if self.n < len(g.V):
				for v in g.succs(self.v_ini):
					if self.n == 0:
						arista_actual = (v_ini, v)
						ds2 = self.ds[:]
						ds2.append(v_ini)
						ds2.append(v)
						yield PartialPS(ds2, arista_actual, v)
					else:
						peso_ultima_arista = d(self.ultima_ar)
						arista_actual = (self.ds[-1], v)
						peso_arista_actual = d(self.ds[-1], v)
						if abs(peso_arista_actual - peso_ultima_arista) <= k:
							ds2 = self.ds[:]
							ds2.append(v)
							yield PartialPS(ds2, arista_actual, v)


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
		# elif g.in_degree(u) > 0 and g.out_degree(v) == 0:
		# 	aristas_a_comprobar[(u, v)] = 1

	# print("Comprobadas",aristas_comprobadas)
	# print("A comprobar",aristas_a_comprobar)

	initialPS = PartialPS([], (), v_ini)
	return BacktrackingSolver.solve(initialPS)


if __name__ == '__main__':
	k, v_ini, nr_aristas, g, d = datos_fichero(filename)
	# for a in g.E:
	# 	print(d(a))
	# print(g.E)
	# print(nr_aristas)
	cml(g,d,v_ini)
	print(cml)

	imprime = False
	for sol in camino_suave_solver(v_ini, g, d, k, nr_aristas):

		imprime = True
		print(sol)

	if not imprime:
		print("No hay solucion")

# for vo in g.V:
# 	for vd in g.succs(vo):
# 		print(d[vo, vd])
