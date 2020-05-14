def pes_bound(i, peso_m, peso_n, b):
	res_m, res_n = [], []
	for o in range(i, len(P)):
		if M - peso_m >= P[o]:
			res_m.append(P[o])
			peso_m += P[o]
		elif N - peso_n >= P[o]:
			peso_n += P[o]
			res_n.append(P[o])
		b += V[o]

	return peso_m, res_m, peso_n, res_n, b


def opt_bound(i, peso_m, peso_n, b):
	indices_ordenados = sorted(range(i, len(P)), key=lambda k: -V[k] / P[k])
	res_m, res_n = [], []
	for i in indices_ordenados:
		peso_act_M = min(float(1), (M - peso_m) / P[i])
		peso_act_N = min(float(1), (N - peso_n) / P[i])

		# si cabe en el contenedor o si dividimos el objeto y cabe en el contenedor
		if M - peso_m > 0 or peso_act_M > 0:
			peso_m += peso_act_M * P[i]
			b += V[i] * peso_act_M
			res_m.append(peso_act_M * P[i])
		elif N - peso_n > 0 or peso_act_N > 0:
			peso_n += peso_act_N * P[i]
			b += V[i] * peso_act_N
			res_n.append(peso_act_N * P[i])
	return peso_m, res_m, peso_n, res_n, b


if __name__ == '__main__':
	P = [1, 2, 3, 4, 5]
	V = [2, 2, 3, 3, 4]
	M = 2.5
	N = 15
	B = 0
	I = 0

	res_pes = pes_bound(I, 0, 0, B)
	print("Cota Pesimista\nPeso M: {}, Pesos en el camion: {} + {}\nPeso N: {}, Pesos en el camion: {} + {}\nCota: {}"
		  .format(res_pes[0], res_pes[1], I, res_pes[2], res_pes[3], I, res_pes[4]))

	res_opt = opt_bound(I, 0, 0, B)

	print("Cota Optimista\nPeso M: {}, Pesos en el camion: {} + {}\nPeso N: {}, Pesos en el camion: {} + {}\nCota: {}"
		  .format(res_opt[0], res_opt[1], I, res_opt[2], res_opt[3], I, res_opt[4]))
