import sys
from algoritmia.datastructures.digraphs import Digraph, WeightingFunction
from al341880.bt_scheme import BacktrackingOptSolver, Solution, Iterable, \
	PartialSolutionWithOptimization, State, PartialSolution, BacktrackingSolver


filename = sys.argv[1]


def datos_fichero(filename):
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
			aristas.append(arista)
			aristas_pesos[arista] = int(arista_peso)

		g = Digraph(E=aristas)
		d = WeightingFunction(aristas_pesos)

		f.close()
	except IOError:
		print("File cannot be open!")

	return k, v_ini, nr_aristas, g, d


def camino_suave_solver(v_ini, g, d, k):
	class PartialPS(PartialSolutionWithOptimization):
		def __init__(self, ds, ar, v_ini):
			self.ds = ds
			self.n = len(ds)
			self.v_ini = v_ini
			self.ultima_ar = ar

		def is_solution(self) -> bool:
			return self.n > 0 and len(g.succs(self.ds[-1])) == 0

		def state(self) -> State:
			return self.ds

		def f(self):
			return -self.n

		def get_solution(self) -> Solution:
			return self.ds

		def successors(self) -> Iterable["PartialSolutionWithOptimization"]:
			for v in g.succs(self.v_ini):
				if self.n == 0:
					arista_actual = (v_ini, v)
					yield PartialPS(self.ds + (v_ini,) + (v,), arista_actual, v)
				else:
					peso_ultima_arista = d(self.ultima_ar)
					arista_actual = (self.ds[-1], v)
					peso_arista_actual = d(self.ds[-1], v)

					if abs(peso_arista_actual - peso_ultima_arista) <= k:
						yield PartialPS(self.ds + (v,), arista_actual, v)

	initialPS = PartialPS((), (), v_ini)
	return BacktrackingOptSolver.solve(initialPS)


if __name__ == '__main__':
	k, v_ini, nr_aristas, g, d = datos_fichero(filename)

	for sol in camino_suave_solver(v_ini, g, d, k):
		print("asd")
		print(len(sol))
		for nr in sol:
			print(nr)
