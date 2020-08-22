def LCS(X, Y):
	def C(i, j):
		if i == 0 or j == 0:
			return 0
		if (i, j) not in mem:
			if i > 0 and j > 0 and X[i - 1] == Y[j - 1]:
				mem[i, j] = (C(i - 1, j - 1) + 1, (i-1, j-1))
			# print(mem[i, j])
			else:
				mem[i, j] = max((C(i - 1, j), (i-1, j)), (C(i, j - 1), (i, j-1)))
		return mem[i, j][0]

	mem = {}
	sol = []
	i, j = len(X), len(Y)
	score = C(i, j)

	while i > 0 and j > 0:
		i, j = mem[i, j][1]
		# esto realmente devuelve la tira de caracteres que son iguales y no el camino original por el que pasa
		# si quieres el camino original, comenta el if y tabula lo de dentro a la izquerda
		if X[i] == Y[j]:
			sol.append((i, j))

	sol.reverse()

	return score, sol


if __name__ == '__main__':
	X = 'abck'
	Y = 'abfk'
	print()
	_, s = LCS(X, Y)

	for x,y in s:
		print(X[x], Y[y])
	print(LCS(X, Y))
