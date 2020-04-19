# Obtener el indice de un minimo local: que sea menor que su vecino izquerdo y derecho


def solve_indice(v):
	def solve(i, j):
		if j - i <= 1:
			return i
		# Indice del medio
		m = i + j // 2

		if v[m] < v[m - 1] and v[m] < v[m + 1]:
			return m
		elif v[m] > v[m - 1]:
			# el min esta en la iz
			return solve(i, m)
		else:
			return solve(m+1, j)

	return solve(0, len(v))


if __name__ == '__main__':
	V = [20, 10, 8, 18, 15, 9, 20]
	print(solve_indice(V))
