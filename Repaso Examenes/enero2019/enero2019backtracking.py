from Utils.bt_scheme import BacktrackingOptSolver, BacktrackingSolver


def numeros_solver(P, T):
	class NumerosPS(BacktrackingOptSolver):
		def __init__(self, ds, suma_local):
			self.ds = ds
			self.n = len(ds)
			self.suma_local = suma_local

		def is_solution(self):
			return self.n == len(P) and self.suma_local == T

		def get_solution(self):
			return self.ds

		def state(self):
			return self.n, self.suma_local

		# lo que dice la f
		def f(self):
			sum = 0
			for nr in self.ds:
				if nr != 0:
					sum += 1
			return sum

		def successors(self):
			if self.n < len(P):
				# for nr in P:
				nr = P[self.n]

				yield NumerosPS(self.ds + (0,), self.suma_local)
				yield NumerosPS(self.ds + (1,), self.suma_local + nr)
				yield NumerosPS(self.ds + (-1,), self.suma_local - nr)

	initial_ps = NumerosPS((), 0)
	return BacktrackingOptSolver.solve(initial_ps)


if __name__ == '__main__':
	P = [12, 1, 10, 4, 9]
	T = 6

	haysol = False
	for sol in numeros_solver(P, T):
		haysol = True
		print(sol)

	if not haysol:
		print("No hay solucion")

