from Utils.bt_scheme import BacktrackingSolver


def domino_solver(f):
	class DominoPS(BacktrackingSolver):
		def __init__(self, ds, fs):
			self.ds = ds
			self.n = len(ds)
			self.fs = fs

		def is_solution(self):
			return self.n == len(f)

		def get_solution(self):
			return self.ds

		def successors(self):
			if self.n < len(f):
				for ficha in self.fs:
					if self.n == 0:
						# copia
						fs2 = self.fs[:]
						fs2.remove(ficha)
						yield DominoPS(self.ds + (ficha, ), fs2)
						# ficha[::-1] da la vuelta a la tupla
						yield DominoPS(self.ds + (ficha[::-1], ), fs2)
					else:
						ultima_ficha = self.ds[-1]
						# comprobamos que b[i] == a[i]
						if ultima_ficha[1] == ficha[0]:  # no hay que girar la ficha
							# copia
							fs2 = self.fs[:]
							fs2.remove(ficha)
							yield DominoPS(self.ds + (ficha, ), fs2)
						# comprobamos que b[i] == b[i]
						elif ultima_ficha[1] == ficha[1]:  # si hay que girar la ficha
							# copia
							fs2 = self.fs[:]
							fs2.remove(ficha)
							yield DominoPS(self.ds + (ficha[::-1],), fs2)
	initialPS = DominoPS((), f)
	return BacktrackingSolver.solve(initialPS)


if __name__ == '__main__':
	F = [(2, 3), (1, 6), (3, 3), (3, 6), (2, 6)]
	imprime = False
	for sol in domino_solver(F):
		imprime = True
		print(sol)

	if not imprime:
		print("No hay solucion")