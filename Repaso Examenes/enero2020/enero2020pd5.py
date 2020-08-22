from Utils.bt_scheme import infinity


def vallado_rec_mem_camino(L, P, S, M, N):
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
					(C(i - 1, m - d * L[i - 1]) + d * P[i - 1], d) for d in range(1, min(m // L[i - 1], S[i - 1]) + 1)
				)
		return mem[i, m][0]

	mem = {}
	sol = []
	i, m = len(L), M
	score = C(i, m)

	if score != infinity:
		while i > 0 and m > 0:
			# print(mem[0, 0][1])
			d = mem[i, m][1]
			m -= d * L[i - 1]
			i -= 1
			sol.append(d)
		sol.reverse()
		return score, sol
	return score


if __name__ == '__main__':
	L = [1, 2, 5, 10]
	P = [100, 200, 500, 1000]
	S = [100, 50, 40, 10]
	M = 20
	N = 4
	print(vallado_rec_mem_camino(L, P, S, M, N))
