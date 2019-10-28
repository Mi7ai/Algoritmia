

__author__ = "Mihai"
__status__ = "Finished"

# Tema 3: ALGORITMOS VORACES


# algoritmo con indices ordenados que sirve solo para ciertos sistemas monetarios


def desglose2(valores, q):
	# ordenamos por valores de mayor a menor
	indices_ordenados = sorted(range(len(valores)), key = lambda i: -valores[i])

	# crear vector resultado con longitud de valores y lleno de ceros
	res = [0]*len(valores)

	# en indices_ordenados tenemos los indices del vector "valores" de mayor a menor
	# valores = [ 4, 2, 6]
	# indices_ordenados será: [2, 0, 1]
	for i in indices_ordenados:
		res[i] = q//valores[i]
		q = q % valores[i]
		if q == 0:
			return res
	return None


if __name__ == '__main__':
	v1 = [1, 2, 5, 10]
	v2 = [2, 5, 10]
	v3 = [1, 9, 15]
	v4 = [2, 9, 15]

	print(desglose2(v1, 6))
	print(desglose2(v2, 7))
	print(desglose2(v3, 19))
	print(desglose2(v4, 10))