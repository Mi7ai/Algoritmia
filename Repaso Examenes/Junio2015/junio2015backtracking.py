from Utils.bt_scheme import BacktrackingSolver, PartialSolutionWithOptimization, PartialSolution
from algoritmia.datastructures.digraphs import UndirectedGraph


def grafo_solver(g, vertices_grafo):
	class CicloHM(PartialSolution):
		def __init__(self, ds):
			self.ds = ds
			self.n = len(ds)
			self.vertices = vertices_grafo

		def is_solution(self):
			return self.n == len(g.V) and self.ds[0] in g.succs(self.ds[-1])

		def get_solution(self):
			return self.ds

		def successors(self):
			if self.n < len(g.V):
				for v in g.succs(self.vertices[self.n]):
					if v not in self.ds:
						yield CicloHM(self.ds + (v,))

	initial_ps = CicloHM(())
	return BacktrackingSolver.solve(initial_ps)


if __name__ == '__main__':
	V = [1, 2, 3, 4, 5]
	E = ((1, 2), (1, 3), (2, 4), (2, 5), (3, 2), (3, 4), (4, 1), (4, 5), (5, 2), (5, 3))
	g = UndirectedGraph(V=V, E=E)

	imprime = False

	for sol in grafo_solver(g, list(g.V)):
		imprime = True
		print(sol)

	if not imprime:
		print("No hay solucion")
