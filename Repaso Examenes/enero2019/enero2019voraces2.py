import random

from algoritmia.datastructures.priorityqueues import MinHeap


def cuerdas(v):
	minheap = MinHeap()
	for elem in v:
		minheap.add(elem)
	coste = 0
	while len(minheap) > 1:
		c1 = minheap.extract_opt()
		c2 = minheap.extract_opt()
		union = c1 + c2
		coste += union
		minheap.add(union)

	return coste


if __name__ == '__main__':
	V1 = [14, 7, 6, 4, 9, 3]

	random.seed(3)
	C = [random.randint(1, 5) for i in range(6)]

	print(cuerdas(V1))  # 106
	print(C)
	print(cuerdas(C))   # 55
