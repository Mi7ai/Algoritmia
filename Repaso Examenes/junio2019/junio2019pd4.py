from Utils.bt_scheme import infinity


def cuerda(L, B, P, M):
	def E(n, m):
		if n == 0:
			return 0

		if n == 0 and m > 0:
			return infinity

		if (n, m) not in mem:
			if n > 0:
				mem[n, m] = max(
					(E(n - 1, m - d * L[n - 1]) + d * B[n - 1], d) for d in range(min(m // L[n - 1], P[n - 1]) + 1))

		return mem[n, m][0]

	mem = {}
	n, m = len(L), M
	score = E(len(L), M)
	sol = []
	while n > 0:
		d = mem[n, m][1]

		m -= d * L[n - 1]
		n -= 1
		sol.append(d)
	sol.reverse()
	return score, sol


if __name__ == '__main__':
	L = [1, 2, 5, 10]
	B = [100, 200, 500, 1000]
	P = [4, 5, 4, 1]
	M = 13
	print(cuerda(L, B, P, M))
