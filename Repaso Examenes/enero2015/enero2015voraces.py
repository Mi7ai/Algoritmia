def galeria(X, D):
	res = [X[0] + D]

	for nr in X:
		if nr > res[-1] + D:
			res.append(nr + D)
	return res


def galeria2(X, D):
	res = []
	if len(X) > 1:
		res.append(X[0])
	else:
		return None

	for i in range(len(X)):
		if res[-1] + D < X[i]:
			res.append(X[i])
	return res


if __name__ == '__main__':
	X = [2, 3, 4, 5, 7, 8, 9, 13, 15]
	D = 2
	print(galeria(X, D),"este no va bien")
	print(galeria2(X, D))
