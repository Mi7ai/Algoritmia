def solve_cuantas_veces(v, x):
	def solve(i, j):
		if j - i < 1:
			if v[i] == x:
				return 1
			return 0
		else:
			m = (i + j) // 2
			return solve(i, m) + solve(m + 1, j)

	return solve(0, len(v) - 1)


# REVISAR

def solve_cuantas_veces2(v, x):
	def solve(i, f):
		if f - i <=1:
			if v[i] == x:
				return i
			if v[f] == x:
				return f

		m = (i + f) // 2
		if v[m] == x:
			return v[m]
		if v[m] > x:
			solve(i, m)
		else:
			solve(m + 1, f)

	return solve(0, len(v) - 1)


if __name__ == '__main__':
	V = [-5, -5, 1, 1, 2, 2, 2, 2, 4, 4, 4, 7]
	X = 4
	print(solve_cuantas_veces2(V, X))
