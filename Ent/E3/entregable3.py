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
			line.strip()
			palabra = line.split(" ")
			datos.append(palabra)

		f.close()
	except IOError:
		print("File cannot be open!")

	return datos


# dictionario = solucion


# pletras: (primeras letra) letras que no pueden ser cero

# def posibles_digitos_dic(lvalidas, d, pletras):
# 	copia_d = copy.deepcopy(d)
# 	nr_asignados_dic = []
# 	# tengo que mirar que numeros tengo para no repetirlos en el diccionario
# 	for v, k in copia_d.items():
# 		nr_asignados_dic.append(k)
#
# 	for l in lvalidas:
# 		# r1 = random.randint(0, 9)
# 		while copia_d.get(l) is None:  # miro si hay letra en el diccionario con un valor asignado
# 			r1 = random.randint(0, 9)
#
# 			if r1 not in nr_asignados_dic:
# 				if l in pletras:
# 					if r1 != 0:  # si la letra es propensa a ser cero y el numero que se le asigna != 0
# 						copia_d[l] = r1
#
# 				else:
# 					copia_d[l] = r1
# 				# yield copia_d
# 				# return copia_d
# 			nr_asignados_dic.append(r1)
# 		return copia_d


# return copia_d


#  lpalabras: letras del fichero
#  d: diccionario que vamos a mirar
#  lvalidas: las letras no repetidas que contiene la linea
#  pletras: la primeras letras que no pueden ser cero


def cryptosolve(linea_palabras):
	class CryptoAPS(PartialSolution):
		def __init__(self, linea, d: dict, lvalidas, pletras):
			self.linea = linea
			# self.solution = solution
			self.d = d
			self.n = len(self.d)

			self.lvalidas = lvalidas
			self.pletras = pletras

		def is_solution(self) -> bool:
			return len(self.lvalidas) == 0 and factible(self.linea, self.d)

		def get_solution(self) -> Solution:
			return self.d

		def successors(self) -> Iterable["PartialSolution"]:
			copia_d = copy.deepcopy(self.d)
			# copia_v = copy.deepcopy(self.lvalidas)
			if len(self.lvalidas) > 0:

				for nr in posibles_en(copia_d):
					l = self.lvalidas[0]
					copia_d[l] = nr
					if factible(self.linea, copia_d):
						yield CryptoAPS(self.linea, copia_d, self.lvalidas[1:], self.pletras)


	# dic_posible = posibles_digitos_dic(self.lvalidas, copia_d, primeras_letras(self.linea))
	# CryptoAPS(self.linea, dic_posible[1:], copia_v[1:], self.pletras)

	dletras = {}

	initialps = CryptoAPS(linea_palabras, dletras, letras_validas(linea_palabras), primeras_letras(linea_palabras))
	return BacktrackingSolver.solve(initialps)


def posibles_en(d: dict):
	posibles = [i for i in range(10)]

	return set(posibles) - set(d.values())


def primeras_letras(linea):
	res = set()
	for p in linea:
		for l in p:
			res.add(l[0])
			break

	return res


def letras_validas(lpalabras):
	m = crear_matriz(lpalabras)
	res = []
	for f in range(len(m)):
		for c in range(len(m[f])):
			if m[f][c] not in res:
				res.append(m[f][c])
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
				if sa >= 10:
					# hay acarreo
					sd = int(str(sa)[1])
					# compruebo suma
					if sd != d.get(m[f][c]):
						return False
					acarreo = int(str(sa)[0])
				if sa < 10 and sa != d.get(m[f][c]):
					return False
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


# le pasas 1 linea y te devuelve las letras ordenadas para meterlas en el dic

def pretty_print(resultado, palabras):
	imprimir = "+".join(palabras[:-1]) + " = " + palabras[-1] + " => "

	# Si solo hay una solución
	if len(resultado) == 1:
		res = resultado[0]
		valor_letras = []

		for p in palabras:
			sol = ""
			for l in p:
				if l in res:
					sol += str(res[l])
				else:
					sol += '@'
			valor_letras.append(sol)

		imprimir += "+".join(valor_letras[:-1]) + " = " + valor_letras[-1]
		print(imprimir)
	# Si hay varias soluciones
	else:
		print(imprimir + str(len(resultado)) + " soluciones")


if __name__ == "__main__":
	lista_palabras = datos_fichero(filename)

	# for linea in lista_palabras:
	# 	sol = list(cryptosolve(linea))
	# 	pretty_print(sol, linea)
	# 	print(sol)
	# [{'a': 7, 'n': 4, 'l': 5, 'e': 1, 'h': 2, 'b': 9, 'c': 6}]

	# # v2
	test1 = ['besa', 'sea', 'eras']
	d = {}
	d['a'] = 2
	d['r'] = 3
	d['e'] = 8
	d['b'] = 9
	d['s'] = 4
	#
	# sol = list(cryptosolve(test1))
	# pretty_print(sol, test1)
	# print(sol)
	# print(factible(lista_palabras[0], d))
	print(factible(test1, d))
	# print(factible(lista_palabras[6], d))
	print("\n<TERMINADO>")
