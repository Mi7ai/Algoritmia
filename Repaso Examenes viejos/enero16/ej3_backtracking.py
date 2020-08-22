from Utils.bt_scheme import PartialSolution, BacktrackingSolver


def sumandos_solver(problema, S):
    class BuscaSumandosPS(PartialSolution):
        def __init__(self, solucion, suma):
            self.solucion = solucion
            self.n = len(self.solucion)
            self.suma = suma

        def is_solution(self):
            return self.n == len(problema) and self.suma == S

        def get_solution(self):
            return self.solucion

        def successors(self):
            if self.n < len(problema):
                for numero in problema[self.n]:
                    if self.suma + numero <= S:
                        yield BuscaSumandosPS(self.solucion + (numero,), self.suma + numero)

    initial_ps = BuscaSumandosPS((), 0)
    return BacktrackingSolver.solve(initial_ps)


if __name__ == '__main__':
    C = [[4,2], [10,6], [8,2]]
    S = 16

    imprime = False
    for sol in sumandos_solver(C, S):
        imprime = True
        print(sol)

    if not imprime:
        print("No hay solucion")


