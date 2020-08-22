def fb():
	for nr in range(1, 100):
		print(nr)
		if nr % 3 == 0:
			print(nr, 'fizz')
		if nr % 5 == 0:
			print(nr, 'buzz')
		if nr % 3 == 0 and nr % 5 == 0:
			print(nr, 'fizzbuzz')


if __name__ == '__main__':
	fb()
