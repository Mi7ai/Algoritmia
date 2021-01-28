from Utils.bt_scheme import infinity


def numeros(N, K):
	def L(k, n):
		if k == 0:
			return 1
		p_max = 0
		# if (n, c) not in mem:
		if k > 0 and n > 0:
			for d in range(1, n):
				p_max = max((p_max, (k - 1, n, 0)),
							(L(k - 1, n - d) * d, (k - 1, n - d, d))
							)

		return p_max

	mem = {}
	sol = []
	k, n = K, N
	score = L(K, N)
	while k != 0:
		k, n, d = mem[k, n][1]
		sol.append(d)
	sol.reverse()
	return score, sol


if __name__ == '__main__':
	N = 6
	K = 3
	print(numeros(N, K))
