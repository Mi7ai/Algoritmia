from random import shuffle


def punto_fijo(a):

    def p(a, i, j):
        if j <= i:
            return None

        m = (i+j)//2
        if a[m] == m:
            return m
        if a[m] > m:
            return p(a, i, m)
        return p(a, m+1, j)
    return p(a, 0, len(a))


a = [5,4,2,3,6,7,8]
print(a)
print(punto_fijo(a))