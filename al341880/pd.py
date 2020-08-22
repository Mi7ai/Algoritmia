
def inversion(N, TDB, BDB, TBT, BBT):
    def L(k, n):
        if n <= 0: return k
        if (k, n) not in mem:
            opcion_A = (L(k, n - 1), (k, n - 1, "A"))
            opcion_B = (L(k - TDB[n - 1], n - 1) * BDB[n - 1], (k - TDB[n - 1], n - 1, "B"))
            if n<6:
                mem[k, n] = max(opcion_A, opcion_B)
            else:
                opcion_C = (L(k - TBT[n - 1], n - 7) * BBT[n - 1], (k - TBT[n - 1], n - 7, "C"))
                mem[k, n] = max(opcion_A, opcion_B, opcion_C)
            #print(opcion_A, opcion_B, opcion_C)
            #print(mem[k, n])
        return mem[k, n][0]

    mem = {}
    ganancia = L(1, N)
    k, n = 1, N
    sol = []
    while n > 0:
        kk, nn, letra = mem[k, n][1]
        sol.append((kk, nn, letra))
        k, n = kk, nn
    sol.reverse()
    return ganancia, sol


if __name__ == '__main__':
    N = 3
    TDB = [0.01, 0.02, 0.02 ]
    BDB = [1.05, 1.04, 1.06 ]
    TBT = [0.2, 0.3, 0.3]
    BBT = [1.1, 1.5, 1.8]
    print(inversion(N, TDB, BDB, TBT, BBT))
