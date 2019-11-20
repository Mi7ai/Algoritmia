import sys
from builtins import list
from typing import *
import random

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
			self.d = {}
			self.usados = set()

		def is_solution(self) -> bool:
			pass

		def get_solution(self) -> Solution:
			pass

		def successors(self) -> Iterable["PartialSolution"]:
			# max_l = max(len(p1), len(p2))
			# print(max_l)

			# print(p1[5])
			pass

	for linea_palabras in lpalabras:
		initialps = CryptoAPS(linea_palabras, ())
		return BacktrackingSolver.solve(initialps)

def primeras_letras(linea):
	res = set()
	for p in linea:
		for l in p:
			res.add(l[0])
			break

	return res


def factible(lpalabras: List[str], d: dict):
	letras_cero = primeras_letras(lpalabras)
	acarreo = 0

	m = crear_matriz(lpalabras)

	for f in range(len(m)):
		sa = 0  #suma anteriores
		sd = 0  #suma digitos
		for c in range(len(m[f])):
			#que exista un valor
			if d.get(m[f][c]) is None:
				return True

			#que la 1ª no sea cero
			if m[f][c] in letras_cero:
				#comprobar si realmente es cero
				if d.get(m[f][c]) == 0:
					return False

			#calculamos suma anteriores
			if c < len(m[f])-1:
				sa += d.get(m[f][c])


			#calcular acarreo
			if c == len(m[f])-1: #estoy en la ultima fila
				sa += acarreo

				#el digito de la suma
				#compruebo si hay acarreo
				if sa == d.get(m[f][c]):
					# no hay acarreo
					# compruebo suma
					acarreo = 0
					continue
				else:
					# hay acarreo
					sd = int(str(sa)[1])
					#compruebo suma
					if sd != d.get(m[f][c]):
						return False
					acarreo = int(str(sa)[0])

	return True


def factible2(lpalabras: List[str], d: dict):
	s_local = 0
	resto = 0
	lpalabras = lpalabras
	suma_nr_anteriores =0
	# for f in range(len(lpalabras[len(lpalabras) - 1])-1, -1, -1):  # la longitud de las columnas = la ultima palabra decr
	for f in range(len(lpalabras[len(lpalabras) - 1])):
		for c in range(len(lpalabras)):

			letras = [letra for letra in reversed(lpalabras[c].strip())]  # cada letra de la palabra con indice c
			# print(d.get(letras[f]))
			if d.get(letras[f]) is None:  # no hay valor asignado
				return True
			elif resto > 0:
				s_local += resto
			if c < len(lpalabras) - 1:
				suma_nr_anteriores += d.get(letras[f])
			s_local += d.get(letras[f])

			if c == len(lpalabras) - 1:  # si estoy en la ultma fila compruebo la suma
				# comprobar si hay resto
				if (s_local % 10) != s_local: #hay resto
					acarreo = int(str(s_local % 10)[0])
					if s_local % 10 != d.get(letras[f]):
						return False
				# s_global = s_local
				if suma_nr_anteriores != letras[f]:
					return False


	# comprobar suma xq estan todas las palabras asignadas con un valor
	return False


def crear_matriz(lpalabras: List[str]):
	# m = [[0]*len(lpalabras[len(lpalabras) - 1]) for i in range(len(lpalabras))]
	# print(m)

	lista_local = []
	for p in lpalabras:
		p = p[::-1]
		p = p.strip()
		lista_local.append(list(p))

	m = []
	for f in range(len(lista_local[len(lista_local) - 1])):
		m.append([])
		for c in range(len(lista_local)):
			if f < len(lista_local[len(lista_local) - 1]):
				try:
					letra = lista_local[c][f]
					m[f].append(letra)
				except :
					continue
	return m


if __name__ == "__main__":
	lista_palabras = datos_fichero(filename)
	# for sol in cryptosolve(lista_palabras):
	# 	print(sol)

	d = {}

	# for l in lista_palabras[0]:
	# 	for p in l:
	# 		for letra in p.split():
	# 			r1 = random.randint(0, 9)
	# 			d[letra] = r1

	d['a'] = 2
	d['á'] = 3
	d['n'] = 4
	d['l'] = 5
	d['e'] = 8
	d['h'] = 2
	d['c'] = 0
	d['b'] = 7
	d['s'] = 8
	d['r'] = 0
	d['t'] = 5
	d['i'] = 1

	test1 = ['atrás','atrás','atrás','atrás','irrita']
	print(factible(test1, d))
	# print(crear_matriz(lista_palabras[0]))
	# print(factible(lista_palabras[6], d))
	print("\n<TERMINADO>")
