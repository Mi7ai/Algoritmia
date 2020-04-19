from Utils.bt_scheme import BacktrackingSolver, PartialSolution
from typing import *


def conjuntos_solver(C, S):
	class ConjuntoPs(BacktrackingSolver):
		def __init__(self, ds, subc):
			self.ds = ds
			self.n = len(ds)
			self.subc = subc

		def is_solution(self):
			return self.n == len(C)

		def get_solution(self):
			return self.ds

		def successors(self):
			if self.n < len(C):
				nr = C[self.n]
				for i in range(S):
					if nr + self.subc[i] <= SUMA:
						subc2 = self.subc[:]
						subc2[i] += nr
						yield ConjuntoPs(self.ds+(i,), subc2)



	SUMA = sum(C) / S
	initialPS = ConjuntoPs((), [0]*S)
	return BacktrackingSolver.solve(initialPS)


if __name__ == '__main__':
	C = [1, 2, 3, 4, 5, 6]
	S = 3
	SUMA = sum(C) / S

	imprime = False
	for sol in conjuntos_solver(C, S):
		imprime = True
		print(sol, SUMA)

	if not imprime:
		print("No hay solucion")