import sys
from typing import TypeVar, List, Iterable
from Utils.skylineviewer import SkylineViewer
from algoritmia.schemes.divideandconquer import DivideAndConquerSolver, IDivideAndConquerProblem, Solution

__author__ = 'Mihai Manea'
__status__ = 'Finished'

T = TypeVar('T')

try:
	filename = sys.argv[1]
except IndexError:
	print("---ERROR---")
	print("Please enter program parameter as follows: |filename with extension| -> test.txt")
	sys.exit(1)


class SkylineSolver(IDivideAndConquerProblem):
	#   Tuple[T, ...]
	def __init__(self, edificios: List[T]):
		self.edificios = edificios

	def is_simple(self) -> "bool":
		return len(self.edificios) <= 1

	def trivial_solution(self) -> "Solution":
		return edificiosAskyline(self.edificios[0])

	def divide(self) -> "Iterable[IDivideAndConquerProblem]":
		yield SkylineSolver(self.edificios[:len(self.edificios) // 2])  # inicio a mitad
		yield SkylineSolver(self.edificios[len(self.edificios) // 2:])  # mitad a final

	def combine(self, solutions: "Iterable[Solution]") -> "Solution":
		res = []
		sk1, sk2 = tuple(solutions)
		i = j = 0
		h1 = h2 = h = 0

		while i < len(sk1) and j < len(sk2):
			if sk1[i][0] < sk2[j][0]:  # si la x de 1 < x de 2
				h1 = sk1[i][1]  # h1 es igual a la altura en ese punto
				h = max(h1, h2)
				punto = (sk1[i][0], h)
				# res.append(punto )
				i += 1
			elif sk1[i][0] == sk2[j][0]:  # x1 == x2
				h1 = sk1[i][1]  # h1 es igual a la altura en ese punto
				h2 = sk2[j][1]  # h2 es igual a la altura en ese punto

				h = max(h1, h2)
				punto = (sk1[i][0], h)  # da igual skyline1 que 2 porque x es igual
				# res.append(punto)
				i += 1
				j += 1
			else:  # x1 > x2
				h2 = sk2[j][1]  # h2 es igual a la altura en ese punto

				h = max(h1, h2)
				punto = (sk2[j][0], h)
				# res.append(punto)
				j += 1

			if len(res) == 0 or h != res[len(res) - 1][
				1]:  # si skyline está vacio o la altura es distinta del ultimo punto añadido
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


def pretty_print(solucion):
	if len(solucion) == 0:
		print(solucion)
	else:
		buildings = []
		# cojo todos los puntos menos el ultimo
		final = len(solucion) - 1
		ini = 0
		for x, y in solucion:
			if ini != final:
				buildings.append(x)
				buildings.append(y)
				print(x, y, end=" ")
				ini += 1
		buildings.append(solucion[len(solucion) - 1][0])
		print(solucion[len(solucion) - 1][0])
		return buildings


if __name__ == "__main__":
	lista_edificios = datos_fichero(filename)

	problem = SkylineSolver(lista_edificios)
	solution = DivideAndConquerSolver().solve(problem)

	if len(sys.argv) == 3 and sys.argv[2] == "-g":
		buildings = pretty_print(solution)
		viewer = SkylineViewer(buildings)
		for b in lista_edificios:
			viewer.add_building(b)
		viewer.run()
	else:
		pretty_print(solution)
