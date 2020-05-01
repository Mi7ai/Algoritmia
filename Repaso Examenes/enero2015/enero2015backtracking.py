from Utils.bt_scheme import BacktrackingVCSolver, PartialSolutionWithVisitedControl


def solver(C, A, B):
	class PartialSolution(BacktrackingVCSolver):
		def __init__(self, ds, SA, SB):
			self.ds = ds
			self.n = len(ds)
			self.SA = SA
			self.SB = SB

		def is_solution(self):
			return self.n == len(C) and self.SA == A and self.SB == B

		def get_solution(self):
			return self.ds

		def state(self):
			return self.n, self.SA, self.SB

		def successors(self):
			if self.n < len(C):
				nr = C[self.n]

				if nr + self.SA <= A:
					yield PartialSolution(self.ds + (1,), self.SA + nr, self.SB)

				if nr + self.SB <= B:
					yield PartialSolution(self.ds + (2,), self.SA, self.SB + nr)

				yield PartialSolution(self.ds + (0,), self.SA, self.SB)

	initialPS = PartialSolution((), 0, 0)
	return BacktrackingVCSolver.solve(initialPS)


if __name__ == '__main__':
	C = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	A = 20
	B = 15
	CA = []
	CB = []
	for sol in solver(C, A, B):
		for i in range(len(sol)):
			if sol[i] == 1:
				CA.append(C[i])
			elif sol[i] == 2:
				CB.append(C[i])
		print("Solucion = {}, CA = {}, CB = {}".format(sol, CA, CB))
	print("C = {}, A = {}, B = {}".format(C, A, B))

