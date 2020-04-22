def busca_indice(v):
	def solve(i, j):
		if j - i <= 1:
			return 1

		m = (i + j) // 2
		if v[m] != v[m - 1] and v[m] != v[m + 1]:
			return v[m]
		elif v[m] != v[m-1]:
			return solve(i, m)
		else:
			return solve(m+1, j)
	return solve(0, len(v))


if __name__ == '__main__':
	v = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]
	print(busca_indice(v))