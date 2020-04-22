def galeria(X, D):
	res = [X[0] + D]

	for nr in X:
		if nr > res[-1] + D:
			res.append(nr + D)
	return res


if __name__ == '__main__':
	X = [2, 3, 4, 9, 13]
	D = 2
	print(galeria(X, D))
