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
	def D(l, n, maximo):
		if n == 0:
			return 0
		if (l, n) not in mem:
			mem[l, n] = (-1, (None, None))
			if maximo != 0 and maximo < L[n - 1]:
				mem[l, n] = max((D(l, n - 1, maximo), (l, n-1)), (D(l, n - 1, L[n - 1]), (l, n-1)))
			else:
				mem[l, n] = (D(l + 1, n - 1, L[n - 1]) + 1, (l, n-1))

		return mem[l,n][0]

	mem = {}
	sol = []

	l, n, maximo = 0, len(L), 0
	score = D(l, n, maximo)
	# print(mem)

	while n > 0:
		l,n = mem[l, n][1]
		sol.append(L[n-1])
		n -= 1

	sol.reverse()
	return score, sol



# def secuencia(L):
# 	def D(n, c):
# 		if n == 0:
# 			return 0
# 		if (n, c) not in mem:
# 			# for i in range(n, c):
# 			if L[n-2] <= L[i-1] and c>0:
# 				mem[n, c] = (D(n - 1, c-1) + 1, 1)
# 			else:
# 				mem[n, c] = (D(n - 1, c) + 0, 0)
# 		return mem[n, c][0]
#
# 	mem = {}
# 	sol = []
#
# 	n, c = len(L), len(L)
# 	score = D(n, c)
#
# 	while n > 0:
# 		d = mem[n, c][1]
# 		ind = sol
# 		sol.append(d)
# 		c -= d
# 		n -= 1
#
# 	sol.reverse()
# 	return score, sol


if __name__ == '__main__':
	L = datos_fichero(filename)
	res = []
	print(L)
	score, sol = secuencia(L)
	# print(score, sorted(sol))
	print(score)
	print(sol)
	for i in range(len(sol)):
		if sol[i] == 1:
			print(L[i - 1])
			res.append(i)
	print(res)
