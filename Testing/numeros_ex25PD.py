from Utils.bt_scheme import infinity


def numeros(N, K):
	def L(k, n):
		if k == 0 and n == 0:
			return 1
		if k == 0 and n > 0:
			return infinity
		# if (n, c) not in mem:
		if k > 0 and n > 0:
			for d in range(max(1,(n//k)+1)):
				print(d)
				return max(L(k-1, n),L(k - 1, n - d) * d)

		return L(k-1, n)
	mem = {}
	sol = []

	score = L(K, N)

	return score, sol


if __name__ == '__main__':
	N = 6
	K = 3
	print(numeros(N, K))
