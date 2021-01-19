from Utils.bt_scheme import infinity


def g(f, c) -> int:
	return f * c


def fondos_rec_mem_camino(D, F, M):
	def B(f, d):
		if f == 0:
			return 0

		if (f, d) not in mem:
			if f > 0 and d < M:
				mem[f, d] = (B(f - 1, d), 0)
			elif f > 0 and d >= M:
				for k in range(M, d):
					mem[f, d] = max((B(f - 1, d),0),(B(f - 1, d - k) + g(f - 1, k), k) )

			return mem[f, d][0]

	mem = {}
	sol = []
	f, d = F, D
	score = B(F, D)

	return score, sol


if __name__ == '__main__':
	F = 4
	D = 13
	M = 2
	print(fondos_rec_mem_camino(D, F, M))
