from Utils.bt_scheme import BacktrackingVCSolver, PartialSolutionWithVisitedControl


def cuerda_solver(L, P, M):
	"""
	Funcion que devuelve la cantidad de vallas de longitud L a usar

	Parameters:
	L (list): longitud cuerdas
	P (list): cantidad cuerdas disponibles
	M (int): longitud de la cuerdas a comprobar

	"""

	class CuerdasPS(PartialSolutionWithVisitedControl):
		def __init__(self, ds, lcuerdas):
			self.ds = ds
			self.n = len(ds)
			self.lcuerdas = lcuerdas

		def is_solution(self):
			return self.n == len(L) and self.lcuerdas == 0

		def get_solution(self):
			return self.ds

		def state(self):
			return self.n, self.lcuerdas

		def successors(self):
			if self.n < len(L):
				for c in range(min(P[self.n], self.lcuerdas // L[self.n]) + 1):
					yield CuerdasPS(self.ds + (c,), self.lcuerdas - (L[self.n] * c))

	initial_ps = CuerdasPS((), M)
	return BacktrackingVCSolver.solve(initial_ps)


if __name__ == '__main__':
	L = [1, 2, 3]
	P = [5, 5, 5]
	M = 9
	imprime = False
	for sol in cuerda_solver(L, P, M):
		imprime = True
		print(sol)

	if not imprime:
		print("No hay solucion")
