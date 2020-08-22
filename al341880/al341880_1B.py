import sys

filename = sys.argv[1]
"""
@author: Mihai Manea
"""

def datos_fichero(filename):
	tdb = []
	bdb = []
	tbt = []
	bbt = []
	meses = 0
	try:
		f = open(filename, "r", encoding="utf-8")
		meses = int(f.readline())
		for i in f.readline().split(" "):
			tdb.append(float(i))
		for i in f.readline().split(" "):
			bdb.append(float(i))
		for i in f.readline().split(" "):
			tbt.append(float(i))
		for i in f.readline().split(" "):
			bbt.append(float(i))

		f.close()
	except IOError:
		print("File cannot be open!")

	return meses, tdb, bdb, tbt, bbt


def inversion_solver(meses, tdb, bdb, tbt, bbt):
	class Inversion:
		def __init__(self, dinero, ds: list):
			self.dinero = dinero
			self.ds = ds

		def a(self):
			return self.dinero

		def b(self, mes):
			return (self.dinero - tdb[mes]) * bdb[mes]

		def c(self, mes):
			return (self.dinero - tbt[mes]) * bbt[mes]

		def exec(self):
			mes = 0
			while mes < meses:
				dinero_a = self.a()
				dinero_b = self.b(mes)
				dinero_c = self.c(mes)

				if mes < meses-6:
					dinero_previsto = max(dinero_a, dinero_b, dinero_c)
				else:
					dinero_previsto = max(dinero_a, dinero_b)

				if dinero_previsto == dinero_a:
					# tomo decision a
					self.ds.append("A")
					self.dinero = dinero_previsto
					mes += 1
				elif dinero_previsto == dinero_b:
					# tomo decision b
					self.ds.append("B")
					self.dinero = dinero_previsto
					mes += 1
				elif dinero_previsto == dinero_c:
					# tomo decision c
					self.ds.append("C")
					self.dinero = dinero_previsto
					mes += 6

			return self.dinero, self.ds

	a = Inversion(1, [])
	dinero, ds = a.exec()

	return dinero, ds


if __name__ == '__main__':
	meses, tdb, bdb, tbt, bbt = datos_fichero(filename)
	# print(tdb, bdb, tbt, bbt)
	dinero, ds = inversion_solver(meses, tdb, bdb, tbt, bbt)

	print(round(dinero, 2))
	print(len(ds))
	for i in ds:
		print(i)
