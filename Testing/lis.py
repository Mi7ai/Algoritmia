def lis(a):
	lis = [0] * len(a)
	# lis[0] = a[0]

	for i in range(0, len(a)):
		max = -1
		for j in range(0, i):
			if a[i] > a[j]:
				if max == -1 and max < lis[j] +1:
					max = a[i]
		if max == -1:
			max = a[i]
		lis[i] = max


	return lis


if __name__ == '__main__':
	A = [2, 3, 5, 4]
	print(lis(A))
