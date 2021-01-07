def fib(n):
	def _fib(n: int):
		if n == 0:
			return 0
		if n == 1:
			return 1
		if n not in mem:
			mem[n] = _fib(n - 2) + _fib(n - 1)
		return mem[n]

	mem = {}
	return _fib(n)


if __name__ == '__main__':
	print(fib(5))
