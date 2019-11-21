import sys
import copy
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


def posibles_digitos_dic(l, copia_d):
	pass


def cryptosolve(lpalabras, total_letras, d, ):
	class CryptoAPS(PartialSolution):
		def __init__(self, linea,  d, lvalidas, pletras):
			self.linea = linea
			# self.solution = solution
			self.n = len(self.solution)
			self.d = d
			self.lvalidas = lvalidas
			self.pletras = pletras


		def is_solution(self) -> bool:
			return len(self.solution) == total_letras

		def get_solution(self) -> Solution:
			return self.solution

		def successors(self) -> Iterable["PartialSolution"]:
			copia_d = copy.deepcopy(self.d)

			for l in self.lvalidas:
				if l not in d:
					#no esta en el dic, miro que valor ponerle
					for dic_posible in posibles_digitos_dic(l, copia_d):

						if factible(self.linea, dic_posible):
							#quitar de lvalidas
							yield CryptoAPS(self.linea, copia_d, self.lvalidas[1:], self.pletras)
					else:
						break



	for linea_palabras in lpalabras:

		initialps = CryptoAPS(linea_palabras, (), d, letras_validas(linea_palabras), primeras_letras(linea_palabras))
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
		sa = 0  # suma anteriores
		sd = 0  # suma digitos
		for c in range(len(m[f])):
			# que exista un valor
			if d.get(m[f][c]) is None:
				return True

			# que la 1ª no sea cero
			if m[f][c] in letras_cero:
				# comprobar si realmente es cero
				if d.get(m[f][c]) == 0:
					return False

			# calculamos suma anteriores
			if c < len(m[f]) - 1:
				sa += d.get(m[f][c])

			# calcular acarreo
			if c == len(m[f]) - 1:  # estoy en la ultima fila
				sa += acarreo

				# el digito de la suma
				# compruebo si hay acarreo
				if sa == d.get(m[f][c]):
					# no hay acarreo
					# compruebo suma
					acarreo = 0
					continue
				else:
					# hay acarreo
					sd = int(str(sa)[1])
					# compruebo suma
					if sd != d.get(m[f][c]):
						return False
					acarreo = int(str(sa)[0])

	return True


def factible2(lpalabras: List[str], d: dict):
	s_local = 0
	resto = 0
	lpalabras = lpalabras
	suma_nr_anteriores = 0
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
				if (s_local % 10) != s_local:  # hay resto
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
				except:
					continue
	return m

#le pasas 1 linea y te devuelve las letras ordenadas para meterlas en el dic


def letras_validas(lpalabras):
	m = crear_matriz(lpalabras)
	res = []
	for f in range(len(m)):
		for c in range(len(m[f])):
			if m[f][c] not in res:
				res.append(m[f][c])
	return res

if __name__ == "__main__":
	lista_palabras = datos_fichero(filename)
	no_usados = set(i for i in range(0, 10))
	d = {}

	for linea_palabras in lista_palabras:
		total_letras = 0

		for palabra in linea_palabras:
			total_letras += len(palabra.strip())

	# for sol in cryptosolve(list(lista_palabras), no_usados, total_letras, d):
	# 	print(sol)

	print(letras_validas(lista_palabras[0]))
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

	test1 = ['atrás', 'atrás', 'atrás', 'atrás', 'irrita']
	print(factible(test1, d))
	# print(crear_matriz(lista_palabras[0]))
	# print(factible(lista_palabras[6], d))
	print("\n<TERMINADO>")
