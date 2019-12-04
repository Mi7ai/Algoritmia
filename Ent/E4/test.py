from typing import TypeVar, List

T = TypeVar('T')  # tipo genérico


def convex_min(a: List[T]) -> T:
	def _min(i: int, k: int) -> T:
		if k - i == 1:
			return a[i]
		elif k - i == 2:
			return min(a[i], a[i + 1])
		else:
			j = (i + k) // 2
			if a[j - 1] < a[j]:
				return _min(i, j)
			else:
				return _min(j, k)

	return _min(0, len(a))


if __name__ == "__main__":
	a = [8.75,8, 6.5, 8.25]
	print(convex_min(a))