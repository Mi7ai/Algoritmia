from Utils.bt_scheme import PartialSolutionWithVisitedControl, BacktrackingVCSolver


def solver(conjunto, A, B):
    class SumaDosEnterosPS(PartialSolutionWithVisitedControl):
        def __init__(self, solucion, sumA, sumB):
            self.solucion = solucion
            self.n = len(self.solucion)
            self.sumA = sumA
            self.sumB = sumB

        def is_solution(self):
            if self.n == len(conjunto):
                return self.sumA == A and self.sumB == B

        def get_solution(self):
            return self.solucion

        def successors(self):
            if self.n < len(conjunto):
                num = conjunto[self.n]

                if self.sumA + num <= A:
                    yield SumaDosEnterosPS(self.solucion + (1,), self.sumA + num, self.sumB)

                if self.sumB + num <= B:
                    yield SumaDosEnterosPS(self.solucion + (2,), self.sumA, self.sumB + num)

                yield SumaDosEnterosPS(self.solucion + (0,), self.sumA, self.sumB)

        def state(self):
            return self.n, self.sumA, self.sumB

    initialPS = SumaDosEnterosPS((), 0, 0)
    return BacktrackingVCSolver.solve(initialPS)

#b)
"""
El metodo successors obtiene el número de C a evaluar. 

Mira si este cabe en el conjunto A y si cabe crea un sucesor sumandole a la suma acumulada
de A su valor y añadiendo un 1 a la solucion (equivale al conjunto A).

Despues mira si el numero cabe en el conjunto B y si cabe crea un sucesor sumandole a la suma
acumulada de B su valor y añadiendo un 2 a la solucion (equivale al conjunto B).

Finalmente, crea un sucesor sin modificar las sumas y con un 0 en la solucion (equivale a 
no ponerlo en ningun conjunto)
"""

#c) PROGRAMA
if __name__ == '__main__':
    C = [3, 1, 15, 18, 14, 23, 11, 10, 17]
    A = 50
    B = 61

    imprime = False
    for sol in solver(C, A, B):
        conjA = []
        conjB = []
        for i in range(len(sol)):
            if sol[i] == 1:
                conjA.append(C[i])
            elif sol[i] == 2:
                conjB.append(C[i])

        imprime = True
        print(sol, conjA, conjB)

    if not imprime:
        print("No hay solucion")