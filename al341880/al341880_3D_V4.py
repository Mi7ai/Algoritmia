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
		if n == -1:
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

	score = F(len(L) - 1, len(L) - 1)
	return score


if __name__ == '__main__':
	L = datos_fichero(filename)
	score = secuencia(L)
	print(score)
