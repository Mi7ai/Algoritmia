def cuerda(L, B, P, M):
	indices_ordenados = sorted(range(len(L)), key=lambda i: -B[i] / L[i])
	res = [0] * len(L)

	for i in indices_ordenados:
		if M // L[i] <= P[i]:
			res[i] = M // L[i]
			M = M % L[i]
		else:
			res[i] = P[i]
			M -= P[i]
	return res


if __name__ == '__main__':
	L = [1, 5, 10, 1]
	B = [1, 6, 1, 2]
	P = [10, 10, 10, 10]
	M = 20
	res = cuerda(L, B, P, M)
	print("{}".format(res))
