from typing import Union, Iterable

from Utils.bt_scheme import BacktrackingOptSolver, BacktrackingSolver, PartialSolutionWithOptimization, Solution, State


def partido_solver(M, K, VS, VN, C):
	class PartidoPS(PartialSolutionWithOptimization):
		def __init__(self, ds, m):
			self.ds = ds
			self.n = len(ds)
			self.m = m

		def is_solution(self) -> bool:
			return self.n == K and self.m == 0

		def get_solution(self) -> Solution:
			return self.ds

		def f(self) -> Union[int, float]:
			suma = 0
			for i in range(self.n):
				if self.ds[i] == 0:
					suma += VN[i]
				elif self.ds[i] == 1:
					suma += VS[i]
			return suma

		def state(self) -> State:
			return self.n, self.m

		def successors(self) -> Iterable["PartialSolutionWithOptimization"]:
			if self.n < K:
				coste = C[self.n]

				# decidir si voy o no
				if coste <= self.m:
					yield PartidoPS(self.ds + (1,), self.m - coste)
				yield PartidoPS(self.ds + (0, ), self.m)

	initial_ps = PartidoPS((), M)
	return BacktrackingOptSolver.solve(initial_ps)


if __name__ == '__main__':
	M = 100
	K = 10
	VS = [i for i in range(10)]
	VN = [i for i in range(10)]
	C = [10, 20, 30, 20, 10, 15, 25, 30, 45, 35]

	for sol in partido_solver(M, K, VS, VN, C):
		print(sol)
		suma = 0
		for i in range(len(sol)):
			if sol[i] == 0:
				suma += VN[i]
			elif sol[i] == 1:
				suma += VS[i]
		print(suma)