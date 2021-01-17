from Utils.bt_scheme import infinity
from typing import *

# LA MOCHILA NO SE TIENE QUE LLENAR TODA


def mochila_parcial_llena_v1(C, V: List[int], W: List[int]):
	def L(n, c):
		if n == 0:
			return 0

		if W[n - 1] <= c:
			return max(L(n-1, c), L(n - 1, c - W[n - 1]) + V[n - 1])

		return L(n - 1, c)

	N = len(V)
	return L(N, C)


def mochila_parcial_llena_v2(C, V, W):
	def L(n, c):
		if n == 0:
			return 0

		if W[n - 1] <= c:
			return max(L(n - 1, c - d * W[n - 1]) + d * V[n - 1] for d in range(1, 2))
		else:
			return L(n - 1, c)

	N = len(V)
	return L(N, C)


if __name__ == "__main__":
	values = [90, 75, 60, 20, 10]
	weights = [4, 3, 3, 2, 2]
	capacity = 6

	print(mochila_parcial_llena_v1(capacity, values, weights))
	print(mochila_parcial_llena_v2(capacity, values, weights))
