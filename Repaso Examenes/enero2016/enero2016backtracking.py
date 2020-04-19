from Utils.bt_scheme import BacktrackingSolver


def lista_solver(C, S):
	class ListaPs(BacktrackingSolver):
		def __init__(self, ds, sumaLocal):
			self.ds = ds
			self.n = len(ds)
			self.sumaLocal = sumaLocal

		def is_solution(self):
			return self.n == len(C) and self.sumaLocal == S

		def get_solution(self):
			return self.ds

		def successors(self):
			if self.n < len(C):
				for i in C[self.n]:
					if i + self.sumaLocal <= S:
						yield ListaPs(self.ds + [i, ], self.sumaLocal + i)

	initialPS = ListaPs([], 0)
	return BacktrackingSolver.solve(initialPS)


if __name__ == '__main__':
	C = [[1, 2, 3], [4, 2, 1], [1, 8, 2]]
	S = 5

	for sol in lista_solver(C, S):
		print(sol)

