from Utils.bt_scheme import infinity


def coin_rec_mem_camino(V, W, Q):
	def L(n, c):
		"""
		:param n: cantidad monedas
		:param c: cantidad a desglosar
		:return: desglose peso minimo
		"""
		if n == 0 and c == 0:
			return 0
		if n == 0 and c > 0:
			return infinity
		if (n, c) not in mem:
			if n > 0 and c >=0:
				mem[n, c] = min((L(n - 1, c - d * V[n - 1]) + d * W[n - 1], d) for d in range(c // V[n - 1] + 1))
		return mem[n, c][0]

	mem = {}
	N = len(v)
	score = L(N, Q)
	sol = []
	n, c = N, Q

	while n > 0:
		d = mem[n, c][1]
		n -= 1
		c -= d * V[n]
		sol.append(d)
	sol.reverse()
	return score, sol

# diferente manera de guardar cosas en el 2º
def coin_rec_mem_camino2(V, W, Q):
	def L(n, c):
		"""
		:param n: cantidad monedas
		:param c: cantidad a desglosar
		:return: desglose peso minimo
		"""
		if n == 0 and c == 0:
			return 0
		if n == 0 and c > 0:
			return infinity
		if (n, c) not in mem:
			if n > 0 and c >=0:
				mem[n, c] = min((L(n - 1, c - d * V[n - 1]) + d * W[n - 1], (n-1, c - d * V[n - 1], d)) for d in range(c // V[n - 1] + 1))
		return mem[n, c][0]

	mem = {}
	N = len(v)
	score = L(N, Q)
	sol = []
	n, c = N, Q

	while n > 0:
		nant, cant, d = mem[n, c][1]
		n = nant
		c = cant
		sol.append(d)
	sol.reverse()
	return score, sol


if __name__ == '__main__':
	v = [1, 2, 5]
	w = [1, 1, 4]
	q = 5
	print(coin_rec_mem_camino(v, w, q))
	print(coin_rec_mem_camino2(v, w, q))
