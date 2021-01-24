import random


def union_cuerdas(c):
	"""Devuelve el coste minimo de unir las cuerdas de c.

	Args:
		c (list): vector de longitudes de cuerdas.

	Returns:
		sum(s) (list): la suma de los costes de las cuerdas.
	"""
	indices_ordenados = sorted(range(len(c)), key=lambda i: c[i])
	s = []
	i = 0
	suma = 0

	while i < len(indices_ordenados) - 1:
		nr1 = indices_ordenados[i]
		nr2 = indices_ordenados[i + 1]
		coste = c[nr1] + c[nr2]
		suma += coste
		if i >= 2:
			s.append(coste)
			s.append(suma)
		else:
			s.append(coste)
		i += 2

	if len(c) % 2 != 0:
		s.append(suma + c[-1])

	return sum(s)


if __name__ == '__main__':
	random.seed(3)
	# C = [random.randint(1, 5) for i in range(6)]
	C = [14, 7, 6, 4, 9]
	print(C)
	print("Coste union: {}".format(union_cuerdas(C)))
