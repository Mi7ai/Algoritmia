from Utils.bt_scheme import PartialSolution, BacktrackingSolver

#b)
def solver(C, S):
    class ParticionesConjuntoPS(PartialSolution):
        def __init__(self, solucion, sumas_acumuladas):
            self.solucion = solucion
            self.sumas_acumuladas = sumas_acumuladas
            self.n = len(self.solucion)

        def is_solution(self):
            return self.n == len(C)

        def get_solution(self):
            return self.solucion

        def successors(self):
            if self.n < len(C):
                nuevo_numero = C[self.n]
                for i in range(S):
                    if self.sumas_acumuladas[i] + nuevo_numero <= suma_maxima:
                        #TODO HACER COPIA DE LA LISTA
                        nueva_lista = self.sumas_acumuladas[:]
                        nueva_lista[i] += nuevo_numero
                        yield ParticionesConjuntoPS(self.solucion + (i,), nueva_lista)

    suma_maxima = sum(C) / S
    sumas_acumuladas = [0] * S

    initialPS = ParticionesConjuntoPS((), sumas_acumuladas)
    return BacktrackingSolver.solve(initialPS)

"""
FUNCIONAMIENTO SUCCESSORS

En el successors, se realiza un bucle por el numero total de subconjuntos a los que puede
ir el número actual. (De 0 a S-1). En cada iteración, se comprueba si el número cabe en 
ese subconjunto. Si cabe, se crea un sucesor y se le pasa la tupla de la solución modificada
y la lista de sumas acumuladas modificada.
"""

#c)
"""
El coste temporal del método successors es O(S).
El coste espacial es O(S^2) y a que en cada iteración del bucle, si se cumple la condicion,
se hace una copia de la lista de sumas acumuladas, que tiene tamaño S.
"""

#d) PROGRAMA
if __name__ == '__main__':
    C = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    S = 5

    imprime = False
    for sol in solver(C, S):
        imprime = True
        print(sol)

    if not imprime:
        print("No hay solucion")
