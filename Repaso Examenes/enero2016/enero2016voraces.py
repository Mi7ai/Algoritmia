# ASUMIMOS QUE beneficios y duraciones estan ordenadas por el ratio beneficio / duracion de mayor a menor

# Mientras quepa con criterio de ordenacion
def cota_pes_subp(dias, beneficios, duraciones):
	ben = 0
	indices_ord = sorted(range(len(beneficios)), key=lambda i: -beneficios[i] / duraciones[i])

	for i in indices_ord:
		if dias >= duraciones[i]:
			dias -= duraciones[i]
			ben += beneficios[i]

	return ben, indices_ord


# Mientras quepa con criterio de ordenacion y fraccionamiento de dias
def cota_opt_subp(dias, beneficios, duraciones):
	ben = 0
	indices_ord = sorted(range(len(beneficios)), key=lambda i: -beneficios[i] / duraciones[i])

	for i in indices_ord:
		dia_actual = duraciones[i]
		ben_actual = beneficios[i]
		f = min(1, dias / dia_actual)
		if f > 0:
			ben += f * ben_actual
			dias -= f * dia_actual

	return ben, indices_ord


if __name__ == '__main__':
	D = 13
	b = [50.0, 100.0, 100.0, 90.0]
	d = [4, 5, 9, 6]

	print(cota_pes_subp(D, b, d))  # 190
	print(cota_opt_subp(D, b, d))  # 215
