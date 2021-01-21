from typing import *


def desglose2(valores: List[int], q: int) -> Optional[List[int]]:
	# creamos vector de índices para recorrer 'valores' de mayor a menor valor
	indices_ordenados = sorted(range(len(valores)), key=lambda i: -valores[i])
	res = [0] * len(valores)
	for i in indices_ordenados:
		print(q,valores[i], q // valores[i])
		res[i] = q // valores[i]
		q = q % valores[i]
		if q == 0:
			return res

	return None


if __name__ == '__main__':
	V = [1, 2, 5, 10]
	Q = 8
	print(desglose2(V, Q))
