from algoritmia.utils import infinity


def coin_change_solve(v, w, Q) -> float:
	def L(q, n):
		if q == 0 and n == 0: return 0
		if q > 0 and n == 0: return infinity
		sol = infinity

		for i in range(q // v[n - 1] + 1):
			# print(q // v[n - 1] + 1)
			q_previo, n_previo = q - i * v[n - 1], n - 1
			sol = min(sol, L(q_previo, n_previo) + i * w[n - 1])
		return sol

	return L(Q, len(v))


def coin_change_mem_solve(v, w, Q) -> float:
	def L(q, n):
		if q == 0 and n == 0: return 0
		if q > 0 and n == 0: return infinity
		if (q, n) not in mem:
			mem[q, n] = infinity
			for i in range(q // v[n - 1] + 1):
				q_previo, n_previo = q - i * v[n - 1], n - 1
				mem[q, n] = min(mem[q, n], L(q_previo, n_previo) + i * w[n - 1])
		return mem[q, n]

	mem = {}
	return L(Q, len(v))


if __name__ == '__main__':
	v, w, q = [1, 2, 5], [1, 1, 4], 2
	print(coin_change_solve(v, w, q))
	print(coin_change_mem_solve(v, w, q))
