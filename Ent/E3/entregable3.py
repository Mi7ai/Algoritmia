import sys
from typing import Iterable
from typing import *

from Utils.bt_scheme import PartialSolution, BacktrackingSolver, Solution

filename = sys.argv[1]


def datos_fichero(filename):
	datos = []
	try:
		f = open(filename, "r", encoding="utf-8")

		for line in f:
			palabra = line.split(" ")
			datos.append(palabra)

		f.close()
	except IOError:
		print("File cannot be open!")

	return datos


# dictionario = solucion


def cryptosolve(lpalabras):
	class CryptoAPS(PartialSolution):
		def __init__(self, linea, solution):
			self.linea = linea
			self.solution = solution
			self.n = len(self.solution)

		def is_solution(self) -> bool:
			pass

		def get_solution(self) -> Solution:
			pass

		def successors(self) -> Iterable["PartialSolution"]:
			pass

	for linea_palabras in lpalabras:
		initialps = CryptoAPS(linea_palabras, ())
		return BacktrackingSolver.solve(initialps)


if __name__ == "__main__":
	lista_palabras = datos_fichero(filename)
	for sol in cryptosolve(lista_palabras):
		print(sol)
	print("\n<TERMINADO>")

