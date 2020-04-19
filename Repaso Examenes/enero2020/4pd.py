

def partido_rec_mem_camino(C, S, N, M):
	def L(n, m):
		if n == 0:
			return 0
		if (n, m) not in mem:
			if n > 0 and m >= C[n-1]:
				mem[n, m] = max((L(n-1, m-d*C[n-1]) + d*S[n-1] +(1-d)*N[n-1], d ) for d in range(2))
			else:
				mem[n, m] = (L(n-1, m), 0)
		return mem[n, m][0]
	# nr votos
	nr = len(S)
	mem = {}
	sol = []
	score = L(nr, M)
	n, m = len(S), M

	while n > 0:
		d = mem[n, m][1]
		sol.append(d)
		n -= 1

	sol.reverse()
	return score, sol


if __name__ == '__main__':
	C = [5,15,8,10]
	S = [5,4,1,6]
	N = [0,0,0,0]
	M = 10
	K = 5
	print(partido_rec_mem_camino(C, S, N, M))