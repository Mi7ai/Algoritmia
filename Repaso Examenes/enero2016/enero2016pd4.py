from Utils.bt_scheme import infinity


def sumando_rec_mem_camino(C, S):
	def L(m, s):
		if m == 0:
			return 0
		for subc in C:
			if (m, s) not in mem:

				for d in range(m):
					if m > 0 and subc[d] <= S:
						mem[m, s] = max(L(m - 1, s), L(m - 1, s - subc[d]))
					else:
						mem[m, s] = L(m - 1, s)

		return mem[m, s][0]

	N = len(C)
	mem = {}
	sol = []
	score = L(len(C[0]), S)

	return score


if __name__ == '__main__':
	C = [[0, 1, 10], [1, 0, 10], [1, 0, 10], [1, 0, 10]]
	S = 40
	print(sumando_rec_mem_camino(C,S))