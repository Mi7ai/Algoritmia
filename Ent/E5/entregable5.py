import sys

try:
	filename = sys.argv[1]
except IndexError:
	print("---ERROR---")
	print("Please enter program parameter as follows: |filename with extension| -> test.txt")
	sys.exit(1)


def datos_fichero(file):
	try:
		f = open(file, "r")
		# k: cantidad de nr que se desean maximizar
		# c: capacidad de la mochila
		# n: cantidad de objetos que van a participar

		k, c, n = f.readline().split(" ")

		# valores
		v = list(f.readline().rstrip('\n').split(" "))

		# pesos -  cambio el nombre a w
		w = list(f.readline().rstrip('\n').split(" "))

		f.close()

	except IOError:
		print("File cannot be open!")

	return k, c, n, v, w


def coin_change_solve(K, C, V, W):
	def coin_change():
		pass

	mem = {}


if __name__ == '__main__':
	k, c, n, v, w = datos_fichero(filename)
	# print(k, c, n, v, w)

	print(coin_change_solve(k, c, v, w))
