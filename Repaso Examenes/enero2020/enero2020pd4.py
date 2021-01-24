def partido_rec_mem_camino(C, S, N, M):
	def L(n, m):

		if n == 0:
			return 0
		if (n, m) not in mem:
			if m >= C[n - 1]:
				mem[n, m] = max((L(n - 1, m - d * C[n - 1]) + d * S[n - 1] + (1 - d) * N[n - 1], d) for d in range(2))
			else:
				mem[n, m] = (L(n - 1, m) + N[n - 1], 0)
		return mem[n, m][0]

	# nr ciudades
	nr = len(S)
	mem = {}
	sol = []
	score = L(nr, M)
	n, m = len(S), M
	# n = len(S)
	while n > 0:
		d = mem[n, m][1]
		sol.append(d)
		m -= d * C[n - 1]
		n -= 1

	sol.reverse()
	return score, sol


if __name__ == '__main__':
	C = [5, 15, 8, 10]
	S = [5, 4, 1, 6]
	N = [3, 5, 6, 4]
	M = 15
	K = 5
	print(partido_rec_mem_camino(C, S, N, M))
