from Utils.bt_scheme import BacktrackingOptSolver, BacktrackingSolver


def numeros_solver(P, T):
	class NumerosPS(BacktrackingSolver):
		def __init__(self, ds, suma_local):
			self.ds = ds
			self.n = len(ds)
			self.suma_local = suma_local

		def is_solution(self):
			return self.n == len(P) and self.suma_local == T

		def get_solution(self):
			return self.ds

		# def state(self):
		# 	return self.n, self.suma_local

		# def f(self):
		# 	sum = 0
		# 	for i in range(len(self.ds)):
		# 		if self.ds[i] == 1:
		# 			sum += self.ds[i] * P[i]
		# 		elif self.ds[i] == -1:
		# 			sum += self.ds[i] * P[i]
		# 	return sum

		def successors(self):
			if self.n < len(P):
				for i in range(self.n, len(P)):
					nr = P[self.n]
					if self.suma_local == T:
						yield NumerosPS(self.ds + (0, ), self.suma_local)
					elif self.suma_local + nr < T:
						yield NumerosPS(self.ds + (-1,), self.suma_local - nr)
					elif self.suma_local + nr > T:
						yield NumerosPS(self.ds + (1,), self.suma_local + nr)

	initial_ps = NumerosPS((), 0)
	return BacktrackingSolver.solve(initial_ps)


if __name__ == '__main__':
	P = [12, 1, 10, 4, 9]
	T = 6

	for sol in numeros_solver(P, T):
		print(sol)

