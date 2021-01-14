L = [1, 2, 5, 10]
B = [100, 200, 500, 1000]
P = [4, 5, 4, 2]
M = 23
n = len(L)

for d in range(min(M // L[n - 1], P[n - 1]) + 1):
	print(min(M // L[n - 1], P[n - 1]) + 1)
	print(d)

	M = (M - d * L[n - 1]) + d * B[n - 1]
	n -= 1
