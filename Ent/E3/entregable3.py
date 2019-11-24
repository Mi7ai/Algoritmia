import sys
import copy
from builtins import list
from typing import *
import random

from Utils.bt_scheme import PartialSolution, BacktrackingSolver, Solution

__author__ ='Mihai Manea'
__status__ = "Finished. Need improvement"

filename = sys.argv[1]


def datos_fichero(filename):
	datos = []
	try:
		f = open(filename, "r", encoding="utf-8")

		for line in f:
			# line.strip()
			palabra = line.split(" ")
			datos.append(palabra)

		f.close()
	except IOError:
		print("File cannot be open!")

	return datos


def cryptosolve(linea_palabras):
	class CryptoAPS(PartialSolution):
		def __init__(self, linea, d: dict, lvalidas: List, pletras):
			self.linea = linea
			self.d = d
			self.lvalidas = lvalidas
			self.pletras = pletras

		def is_solution(self) -> bool:
			return len(self.lvalidas) == 0

		def get_solution(self) -> Solution:
			if self.is_solution():
				return self.d

		def successors(self) -> Iterable["PartialSolution"]:
			if len(self.lvalidas) > 0:
				for nr in posibles_en(self.d):
					copia_d = copy.deepcopy(self.d)
					letra = self.lvalidas[0]
					copia_d[letra] = nr
					if factible(self.linea, copia_d):
						yield CryptoAPS(self.linea, copia_d, self.lvalidas[1:], self.pletras)

	dletras = {}
	initialps = CryptoAPS(linea_palabras, dletras, letras_validas(linea_palabras), primeras_letras(linea_palabras))
	return BacktrackingSolver.solve(initialps)

# devuelve los valores que puede tomar el diccionario


def posibles_en(d: dict) -> set:
	posibles = [i for i in range(10)]

	return set(posibles) - set(d.values())

# devuelve las primeras letras de cada palabra que no pueden ser cero


def primeras_letras(linea) -> List:
	res = set()
	for p in linea:
		for l in p:
			res.add(l[0])
			break

	return res

# devuelve las letras que contiene la linea sin duplicar


def letras_validas(lpalabras) -> List:
	m = crear_matriz(lpalabras)
	res = []
	for f in range(len(m)):
		for c in range(len(m[f])):
			if m[f][c] not in res:
				res.append(m[f][c])
	return res

# mira si una linea es factible o no


def factible(lpalabras: List[str], d: dict) -> bool:
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
			if m[f][c] in letras_cero and d.get(m[f][c]) == 0:
				# comprobar si realmente es cero

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
					break
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


# le pasas 1 linea y te devuelve las letras ordenadas para meterlas en el dic


def crear_matriz(lpalabras: List[str]):
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

# imprime las soluciones tal y como se piden


def pretty_print(nr, resultado, palabras):
	imprimir = "+".join(palabras[:-1]) + " = " + palabras[-1] + " => "

	# 1 solución
	if len(resultado) == 1:
		res = resultado[0]
		valor_letras = []

		for p in palabras:
			sol = ""
			for l in p:
				sol += str(res[l])
			valor_letras.append(sol)

		imprimir += "+".join(valor_letras[:-1]) + " = " + valor_letras[-1]
		print(imprimir)
	# + soluciones
	else:
		print(imprimir + str(len(resultado)) + " soluciones")


if __name__ == "__main__":
	###
	# crea las lines sin el \n
	# ----------------------------------------
	lista_palabras = []
	p = []
	for linea in datos_fichero(filename):
		for palabra in linea:
			p.append(palabra.strip())

		lista_palabras.append(list(p))
		p.clear()
	# ----------------------------------------

	###
	# Imprime soluciones
	# ----------------------------------------
	for linea in lista_palabras:
		sol = list(cryptosolve(linea))
		pretty_print(len(sol), sol, linea)
	# ----------------------------------------

	print("\n<TERMINADO>")
