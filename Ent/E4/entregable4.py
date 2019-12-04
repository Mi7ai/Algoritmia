import sys
from typing import TypeVar, List, Tuple, Iterable
from Utils.skylineviewer import SkylineViewer
from algoritmia.schemes.divideandconquer import DivideAndConquerSolver, IDivideAndConquerProblem, Solution

T = TypeVar('T')

try:
	filename = sys.argv[1]
except IndexError:
	print("---ERROR---")
	print("Please enter program parameter as follows: |filename with extension| -> test.txt")
	sys.exit(1)


class SkylineSolver(IDivideAndConquerProblem):
	#   Tuple[T, ...]
	def __init__(self, skiline: List[T]):
		self.skyline = skiline

	def is_simple(self) -> "bool":
		return len(self.skyline) <= 1

	def trivial_solution(self) -> "Solution":
		return self.skyline

	def divide(self) -> "Iterable[IDivideAndConquerProblem]":
		yield SkylineSolver(self.skyline[:len(self.skyline) // 2])  # inicio a mitad
		yield SkylineSolver(self.skyline[len(self.skyline) // 2:])  # mitad a final

	def combine(self, solutions: "Iterable[Solution]") -> "Solution":
		res = []
		sk1, sk2 = solutions
		i = j = 0
		h1 = h2 = h = 0

		while i < len(sk1) and j < len(sk2):
			if sk1[i][0] < sk2[j][0]:  # si la x de 1 < x de 2
				h1 = sk1[i][1]  # h1 es igual a la altura en ese punto
				h = max(h1, h2)
				punto = (sk1[i][0], h)
				# res.append(punto, h)
				i += 1
			elif sk1[i][0] == sk2[j][0]:  # x1 == x2
				h1 = sk1[i][1]  # h1 es igual a la altura en ese punto
				h2 = sk2[j][1]  # h2 es igual a la altura en ese punto

				h = max(h1, h2)
				punto = (sk1[i][0], h)  # da igual skyline1 que 2 porque x es igual
				# res.append(punto, h)
				i += 1
				j += 1
			else:  # x1 > x2
				h2 = sk2[j][1]  # h2 es igual a la altura en ese punto

				h = max(h1, h2)
				punto = (sk2[j][0], h)
				# res.append(punto, h)
				j += 1

			if len(res) == 0 or h != res[len(res) - 1][1]:  # si skyline está vacio o la altura es distinta del ultimo punto añadido
				res.append(punto)

		while i < len(sk1):
			res.append(sk1[i])
			i += 1

		while j < len(sk2):
			res.append(sk2[j])
			j += 1

		return res


def datos_fichero(filename):
	datos = []
	try:
		f = open(filename, "r")

		for l in f:
			linea = l.rstrip('\n').split(" ")

			datos.append(tuple((int(linea[0]), int(linea[1]), int(linea[2]))))
		f.close()

	except IOError:
		print("File cannot be open!")

	return datos


def edificiosAskyline(edificio):
	res = []
	coordenada = (int(edificio[0]), int(edificio[1]))
	coordenada2 = ((int(edificio[0]) + int(edificio[2])), 0)
	res.append(coordenada)
	res.append(coordenada2)
	return res


if __name__ == "__main__":
	lista = datos_fichero(filename)
	l = []
	l.append(lista[0])
	l.append(lista[1])
	l.append(lista[2])
	# ed = []
	sk1 = edificiosAskyline(lista[0])
	sk2 = edificiosAskyline(lista[1])
	sk3 = edificiosAskyline(lista[2])
	sk4 = edificiosAskyline(lista[3])


	problem = SkylineSolver(sk1+sk2)

	solution = DivideAndConquerSolver().solve(problem)
	print(solution)
