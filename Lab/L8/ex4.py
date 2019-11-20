import typing

# no esta completo
def max_suma(a):
    if len(a) == 1:
        return a

    def _max_suma(a, i, j):
        m = (i + j) // 2
        ac = a[m]
        sc = a[m]  # suma centro
        bc = m  # beginning centro
        ec = m + 1  # end centro

        for k in range(m + 1, j):
            ac += k  # suma acumulada
            if ac > sc:
                sc = ac
                ec = k + 1
        ac = sc
        for k in range(m - 1, i - 1, -1):
            ac += k  # suma acumulada
            if ac > sc:
                sc = ac
                bc = k
        sr, br, er = _max_suma(a, m+1, j)
        sl, bl, el = _max_suma(a, i, m-1)