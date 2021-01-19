from Utils.bt_scheme import BacktrackingOptSolver, PartialSolutionWithOptimization


def vallado_solver(L, C, P, M):
	"""
	Funcion que devuelve el coste minimo de vallas

	Parameters:
	L (list): longitud vallas
	C (list): cantidad vallas disponibles
	P (list): precio por valla
	M (int): longitud de la valla a comprobar

	"""

	class ValladoPs(PartialSolutionWithOptimization):
		def __init__(self, ds, longitud_local):
			self.ds = ds
			self.n = len(ds)
			self.longitud_local = longitud_local

		def is_solution(self):
			return self.n == len(L) and self.longitud_local == 0

		def get_solution(self):
			return self.ds

		def state(self):
			return self.n, self.longitud_local

		def f(self):
			sum = 0
			for i in range(len(self.ds)):
				sum += P[i] * self.ds[i]
			return sum

		def successors(self):
			if self.n < len(L):

				for c in range(0, min(C[self.n], self.longitud_local // L[self.n]) + 1):
					if c <= self.longitud_local:
						yield ValladoPs(self.ds + (c,), self.longitud_local - (L[self.n] * c))

	initial_ps = ValladoPs((), M)
	return BacktrackingOptSolver.solve(initial_ps)


if __name__ == '__main__':
	L = [1, 2, 3]
	C = [5, 5, 5]
	P = [10, 8, 5]
	M = 4
	imprime = False
	for sol in vallado_solver(L, C, P, M):
		imprime = True
		print(sol)

	if not imprime:
		print("No hay solucion")
