from typing import List

from Utils.bt_scheme import infinity


def colocar_vallas(l, p, s, M):
	def C(m, i) -> int:
		if i == 0 and m == 0:
			return 0
		if i == 0 and m > 0:
			return infinity
		if i > 0 and m < l[i-1]:
			return infinity

		if (i, m) not in mem:
			if i > 0 and m >= l[i - 1]:
				for j in range(1,min(s[i], m // l[i-1])+1):
					i_previo = i - 1
					m_previo = m - j * l[i-1]

					mem[i, m] = min(
									(C(i_previo, m_previo) + j * p[i-1], (i_previo, m_previo, j)))

		return mem[i, m][0]


	mem = {}
	precio = C(M, len(l))
	sol = []
	i, m = len(l), M

	while i != 0:
		_, (i_previo, m_previo, j) = mem[i, m]
		sol.append(j)
		i, m = i_previo, m_previo

	sol.reverse()
	return precio, sol


if __name__ == '__main__':
	M = 10
	L = [1, 2, 5, 10]
	P = [1, 2, 3, 4]
	S = [10, 8, 5, 5]

	print(colocar_vallas(L, P, S, M))
