from typing import List

from Utils.bt_scheme import infinity


def colocar_vallas(n, l, p, s, M):
    def C(m, i) -> int:
        if i == 0 and m == 0:
            return 0
        if i == 0 and m > 0:
            return infinity
        if i > 0 and m < l[i]:
            return infinity

        if (i, m) not in mem:
            mem[i, m] = infinity, ()

            for j in range(min(s[i], m // l[i])):
                i_previo = i - 1
                m_previo = m - j * l[i]

                mem[i, m] = min(mem[i, m],
                                (C(i_previo, m_previo) + j * p[i], (i_previo, m_previo, j)))

        return mem[i, m][0]

    N = len(n)
    mem = {}
    precio = C(N, M)
    sol = []
    i, m = N, M

    while i != 0:
        _, (i_previo, m_previo, j) = mem[i, m]
        sol.append(j)
        i, m = i_previo, m_previo

    sol.reverse()
    return precio, sol
