def numeros(V, a):
	res = []
	v = sorted(range(len(V)), key=lambda i: V[i])
	long = len(V)

	i = 0
	ini = V[v[0]]
	fin = ini + a
	res.append([ini, fin])
	while long > 0:
		# nr actual
		nr = V[v[i]]
		if nr > fin:
			ini = nr
			fin = ini + a
			res.append([ini, fin])
		long -= 1
		i += 1
	return res


def numeros2(f, a):
	res = []
	ini = f[0]
	fin = ini + a
	res.append([ini, fin])
	indices_ordenados = sorted(range(len(V)), key=lambda i: f[i])

	for i in indices_ordenados:
		if f[i] > fin:
			ini = f[i]
			fin = ini + a
			res.append([ini, fin])

	return res


if __name__ == '__main__':
	V = [1.0, 3.5, 9.0, 2.5, 7.0, 12.0, 13.0, 15.0]
	A = 3.0
	print(numeros(V, A))
	print(numeros2(V, A))
