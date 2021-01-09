from random import seed, randrange
from typing import *


def recursos_rec_mem_camino(v: Dict[Tuple[int, int], int], m: List[int], U: int) -> Tuple[int, List[int]]:
	def B(n: int, u: int) -> int:
		# --------------------
		if n == 0:
			return 0
		if (n, u) not in mem:
			if u >= 0 and n >= 0:
				mem[n, u] = max((B(n - 1, u - k) + v[n - 1, k], (n-1,k)) for k in range(min(m[n - 1], u) + 1))
		return mem[n, u][0]
		# --------------------

	N = len(m)
	mem = {}
	score = B(N, U)
	sol = []
	# --------------------
	n, u = N, U
	while n > 0 and u > 0:
		nant, k = mem[n, u][1]
		sol.append(k)
		n = nant
		u -= k
	sol.reverse()
	# --------------------
	return score, sol


if __name__ == '__main__':
	U = 12  # número de unidades de recurso disponibles
	m = [2, 4, 2, 4, 2]  # número máximo de recursos que podemos asignar a cada actividad
	seed(0)
	v = dict(((i, u), randrange(100)) for i in range(len(m)) for u in range(0, U + 1))

	print(recursos_rec_mem_camino(v, m, U))