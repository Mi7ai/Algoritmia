from Utils.bt_scheme import infinity


def funcion_palabras(W, C, l):
    def P(j):
        if j == 0:
            return 0

        if j not in mem:
            mem[j] = infinity

            for i in range(j):
                if j - i + 1 + sum(W[k] for k in range(i, j)) <= C:
                    mem[j] = min(mem[j],
                                 P(i) + l(j - i - 1 + sum(W[k] for k in range(i, j)), C))

        return mem[j]

    mem = {}

    score = P(len(W))

    return score

