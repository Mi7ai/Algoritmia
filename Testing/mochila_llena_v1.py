from algoritmia.utils import infinity
from typing import *

# LA MOCHILA SE TIENE QUE LLENAR TODA


def mochila_llena_v1(c, v: List[int], w:List[int]):
	def L(n: int, c: int):
		if n == 0:
			return 0
		if n == 0 and c > 0:
			return - float("infinity")
		if w[n - 1] <= c:
			return max(L(n - 1, c - w[n - 1]) + v[n - 1])

		return L(n - 1, c)


	N = len(v)
	return L(N, c)


def mochila_llena_v2(C, V, W):
	def L(n, c):
		if n == 0:
			return 0
		if n == 0 and c > 0:
			return - float(infinity)

		if W[n - 1] <= c:
			return max(L(n - 1, c - d * W[n - 1]) + d * V[n - 1] for d in range(0, 2))

		return L(n - 1, c)

	N = len(V)
	return L(N, C)

def mochila_rec(v: List[int], w: List[int], C: int) -> int:
    def B(n: int, c: int) -> int:
        # --------------------
        if n == 0:
            return 0
        if w[n-1] <= c:  # si el peso del objeto <= capacidad mochila
            # miro el objeto anterior con la misma capacidad
            # miro el objeto anterior con con ca capacidad - el peso del objeto + el valor del objeto
            return max(B(n-1, c), B(n-1, c-w[n-1]) + v[n-1])
        # si no cabe, miro el objeto anterior con la misma capacidad
        return B(n-1, c)
        # --------------------

    N = len(v)
    return B(N, C)
if __name__ == "__main__":
	values = [90, 75, 60, 20, 10]
	weights = [4, 3, 3, 2, 2]
	capacity = 10

	print(mochila_llena_v1(capacity, values, weights))
	print(mochila_rec(values, weights, capacity))
