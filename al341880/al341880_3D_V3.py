import sys

filename = sys.argv[1]


def datos_fichero(filename):
	datos = []
	try:
		f = open(filename, "r", encoding="utf-8")
		nr_elementos = f.readline()
		for line in f:
			datos.append(int(line.strip()))

		f.close()
	except IOError:
		print("File cannot be open!")

	return datos


def secuencia(L):
	def F(p, n):
		if n == 0:
			return 0
		if (p, n) not in mem:
			if n == p:
				mem[p, n] = max((F(n - 1, n - 1), (n - 1, n - 1)), (F(n, n - 1) + 1, (n, n - 1)))
			elif n != p and L[p] > L[n]:
				mem[p, n] = max((F(p, n - 1), (p, n - 1)), (F(n, n - 1) + 1, (n, n - 1)))
			elif n != p and L[p] <= L[n]:
				mem[p, n] = (F(p, n - 1), (p, n - 1))
		return mem[p, n][0]

	mem = {}
	sol = []

	score = F(len(L) - 1, len(L) - 1)
	p, n = len(L) - 1, len(L) - 1
	print(mem)
	while p > 0 and n > 0:
		i2, (_, _) = mem[p, n]
		# sol.append(mem[p2, n2])
		# if L[i2] not in sol:
		sol.append(L[i2])
		n -= 1
		p -= 1
	sol.reverse()
	return score, sol


if __name__ == '__main__':
	L = datos_fichero(filename)
	D = [0] * len(L)
	res = []

	# print(D)
	score, sol = secuencia(L)
	print("vector", L)
	print("score", score)
	print("sol", sol)
