def mineros(V):
	def L(n, c):
		if n == 0:
			return 0
		if (n, c) not in mem:
			if n > 0 and c >= V[n - 1]:
				mem[n, c] = (L(n - 1, c - 1 * V[n - 1]) + 1 * V[n - 1], 1)
			else:
				mem[n, c] = (L(n - 1, c), 0)
		return mem[n, c][0]

	mem = {}
	sol = []

	n, c = len(V), sum(V) / 2
	# CAMBIAR AQUI
	score = L(n, c)

	while n > 0:
		dec = mem[n, c][1]
		sol.append(dec)
		c -= dec * V[n - 1]
		n -= 1
	sol.reverse()
	return score, sol


def mineros2(V):
	def L(n, c):
		if n == 0:
			return 0
		if (n, c) not in mem:
			if n > 0 :
				mem[n, c] = min((L(n - 1, c - d * V[n - 1]) + d * V[n - 1], d) for d in range(2))
			else:
				mem[n, c] = (L(n - 1, c - 1 * V[n - 1]) + 1 * V[n - 1],  1)
		return mem[n, c][0]

	mem = {}
	sol = []

	n, c = len(V), sum(V) / 2
	# CAMBIAR AQUI
	score = L(n, c)

	while n > 0:
		dec = mem[n, c][1]
		sol.append(dec)
		c -= dec * V[n - 1]
		n -= 1
	sol.reverse()
	return score, sol


if __name__ == '__main__':
	V = [2, 4, 3, 6, 4, 4, 5, 7, 8]
	print(mineros(V))
	print(mineros2(V))