import sys
sys.path.append('.')


def fib_mem(n: int) -> int:
	def _f(n: int) -> int:
		global steps

		steps += 1
		if n == 0: return 0
		if n == 1: return 1
		if n not in mem:
			mem[n] = _f(n - 2) + _f(n - 1)
		return mem[n]

	mem = {}
	return _f(n)


def fib_iter(n: int) -> int:
	mem = {}
	steps = 0
	for i in range(n+1):
		steps += 1
		if i == 0:
			mem[i] = 0
		if i == 1:
			mem[i] = 1
		if i not in mem:
			mem[i] = mem[i - 2] + mem[i - 1]

	# return mem[n]

	print('Fib de', n, 'es = >', mem[n], "steps:", steps)


steps = 0
print(fib_mem(20), steps)
fib_iter(20)
