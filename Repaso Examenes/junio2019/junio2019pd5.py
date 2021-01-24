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
			else:
				mem[f, d] = max((B(f - 1, d - k) + g(f - 1, k), k) for k in range(M, d + 1))

		return mem[f, d][0]

	mem = {}
	sol = []
	f, d = F, D
	score = B(F, D)

	while f > 0:
		k = mem[f, d][1]
		sol.append(k)
		d -= k
		f -= 1

	sol.reverse()
	return score, sol


def fondos_rec_mem_camino2(D, F, M):
	def B(f, d):
		if f == 0:
			return 0

		if (f, d) not in mem:
			if f > 0 and d < M:
				mem[f, d] = (B(f - 1, d), (f-1,d,0))
			else:
				mem[f, d] = max((B(f - 1, d - k) + g(f - 1, k), (f - 1, d - k, k)) for k in range(M, d + 1))

		return mem[f, d][0]

	mem = {}
	sol = []
	f, d = F, D
	score = B(F, D)

	while f > 0:
		f, d, k = mem[f, d][1]
		sol.append(k)

	sol.reverse()
	return score, sol


if __name__ == '__main__':
	F = 4
	D = 13
	M = 2
	print(fondos_rec_mem_camino(D, F, M))
	print(fondos_rec_mem_camino2(D, F, M))
