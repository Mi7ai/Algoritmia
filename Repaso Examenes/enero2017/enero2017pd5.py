from Utils.bt_scheme import infinity


def vallado_rec_mem_camino(M, L, P, S):
	def C(i, m):
		if i == 0 and m == 0:
			return 0

		if i == 0 and m > 0:
			return infinity

		if i > 0 and m < L[i - 1]:
			return infinity

		if (i, m) not in mem:
			if i > 0 and m >= L[i - 1]:
				mem[i, m] = min(
					(C(i - 1, m - j * L[i - 1]) + j * P[i - 1], j) for j in range(1, min(m // L[i - 1], S[i - 1]) + 1)
				)
		return mem[i, m][0]

	mem = {}
	sol = []
	i, m = len(L), M
	score = C(i, m)

	while i > 0 and m > 0:
		j = mem[i, m][1]
		sol.append(j)
		m -= j * L[i - 1]
		i -= 1
	sol.reverse()
	return score, sol


def vallado_rec_mem_camino2(M, L, P, S):
	def C(i, m):
		if i == 0 and m == 0:
			return 0

		if i == 0 and m > 0:
			return infinity

		if i > 0 and m < L[i - 1]:
			return infinity

		if (i, m) not in mem:
			if i > 0 and m >= L[i - 1]:
				mem[i, m] = min(
					(C(i - 1, m - j * L[i - 1]) + j * P[i - 1], (i - 1, m - j * L[i - 1], j)) for j in range(1, min(m // L[i - 1], S[i - 1])+1)
				)
		return mem[i, m][0]

	mem = {}
	sol = []
	i, m = len(L), M
	score = C(i, m)

	while i > 0:
		iant, mant, j = mem[i, m][1]
		sol.append(j)
		m = mant
		i = iant
	sol.reverse()
	return score, sol


if __name__ == '__main__':
	# obligatorio mayor que la suma de longitudes

	M = 10
	L = [1, 2, 5]
	P = [1, 2, 3]
	S = [10, 10, 10]

	print(vallado_rec_mem_camino(M, L, P, S))
