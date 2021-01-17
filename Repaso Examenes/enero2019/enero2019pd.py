from Utils.bt_scheme import infinity


def numeros_solver(P, T):
	def L(n, t) -> int:
		if n == 0:
			return 0
		# if n == 0 and t > 0:
		# 	return infinity
		if (n, t) not in mem:
			if n > 0:
				mem[n, t] = min((L(n - 1, t - d * P[n - 1]) + d, d) for d in range(-1, 2))

		return mem[n, t][0]

	mem = {}
	sol = []
	n, t = len(P), T
	score = L(n, t)

	while n > 0:
		d = mem[n, t][1]
		sol.append(d)
		if d > 0:
			t -= d * P[n - 1]
		else:
			t += d * P[n - 1]
		n -= 1
	sol.reverse()

	return score, sol


if __name__ == '__main__':
	P = [12, 1, 10, 4, 9]
	T = 6
	print(numeros_solver(P, T))
