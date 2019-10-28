

__author__ = "Mihai"
__status__ = "Finished"

# Tema 3: ALGORITMOS VORACES


# esta bien pero el algoritmo no devuelve una solucion buena


def desglose1(valores, q):
	res = []
	for v in valores:
		res.append(q//v)
		q = q%v
		if q == 0:
			return res + [0]*(len(valores)-len(res))
	return None


if __name__ == '__main__':
	v1 = [1, 2, 5, 10]
	v2 = [2, 5, 10]
	v3 = [1, 9, 15]

	print(desglose1(v1, 6))
	print(desglose1(v2, 7))
	print(desglose1(v3, 9))