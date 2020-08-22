from Utils.bt_scheme import infinity

def desglose(v, w, m, Q):
    def L(q, n):
        if q == 0 and n == 0:
            return 0
        if q > 0 and n == 0:
            return infinity

        if (q,n) not in mem:
            mem[q,n] = infinity, ()

            #TODO SUMARLE UNO AL RANGE PQ ACABA UNO ANTES
            for i in range(min(m[n-1], q // v[n-1]) + 1):
                q_prev = q - i * v[n-1]
                n_prev = n - 1

                mem[q, n] = min (mem[q,n], (L(q_prev, n_prev) + i * w[n-1], (q_prev, n_prev, i)))

        return mem[q,n][0]

    mem = {}

    peso = L(Q, len(v))
    q, n = Q, len(v)

    sol = []

    while (q,n) != (0,0):
        _, (q_prev, n_prev, i) = mem[q,n]
        sol.append(i)
        q, n = q_prev, n_prev

    sol.reverse()
    return peso, sol





