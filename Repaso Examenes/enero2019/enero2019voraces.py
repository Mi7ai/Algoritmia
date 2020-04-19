def cuerda(L, B, P, M):
	indices_ordenados = sorted(range(len(L)), key=lambda i: -P[i]/L[i])
	res = [0]*len(L)

	for i in indices_ordenados:
		if M//L[i] <= P[i]:
			res[i] = M//L[i]
			M = M % L[i]
		else:
			res[i] = P[i]
			M -= P[i]
	return res


if __name__ == '__main__':
	L = [1,5,10,1]
	B = [5,4,1,6]
	P = [10,10,10,10]
	M = 20
	res = cuerda(L, B, P, M)
	print("{} resto: {}".format(res,M-sum(res)))
