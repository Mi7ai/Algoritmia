from Utils.bt_scheme import PartialSolutionWithOptimization, BacktrackingOptSolver, State, Solution
from typing import *
from random import random, seed


def knapsack_solve(weights, values, capacity):
    class KnapsackPS(PartialSolutionWithOptimization):
        def __init__(self, pending, solution):         # IMPLEMENTAR: Añade los parámetros que tú consideres
            self.pending = pending
            self.n = len(solution)
            self.solution = solution
            pass

        def is_solution(self) -> bool:      # IMPLEMENTAR
            return len(self.solution) == len(weights)

        def get_solution(self) -> Solution: # IMPLEMENTAR
            return self.solution

        def successors(self) -> Iterable["KnapsackPS"]:# IMPLEMENTAR
            if self.n < len(values):
                if weights[self.n] <= self.pending  :
                    yield KnapsackPS(self.pending - weights[self.n], self.solution + (1,))
                yield KnapsackPS(self.pending, self.solution + (0,))

        def state(self) -> State:           # IMPLEMENTAR
            # return len(self.solution), sum(self.solution[i] * weights[i] for i in range(len(self.solution)) )
            return len(self.solution), self.pending

        def f(self) -> Union[int, float]:   # IMPLEMENTAR
            # sum = 0
            # for s in range(len(self.solution)):
            #     sum += self.solution[s] * values[s]
            # return -sum
            return -sum(self.solution[i] * values[i] for i in range(len(self.solution)) )

    initialPS = KnapsackPS(capacity, ())                # IMPLEMENTAR: Añade los parámetros que tú consideres
    return BacktrackingOptSolver.solve(initialPS)


def create_knapsack_problem(num_objects: int) -> Tuple[Tuple[int,...], Tuple[int,...], int]:
    seed(42)
    weights = [int(random()*1000+1) for _ in range(num_objects)]
    values = [int(random()*1000+1) for _ in range(num_objects)]
    capacity = sum(weights)//2
    return weights, values, capacity


# Programa principal ------------------------------------------
if __name__ == "__main__":
    # W, V, C = [1, 4, 2, 3], [2, 3, 4, 2], 7     # SOLUCIÓN: Weight=7,    Value=9
    W, V, C = create_knapsack_problem(30)     # SOLUCIÓN: Weight=6313, Value=11824
    for sol in knapsack_solve(W, V, C):
        print (sol)
        print ("Weight:", sum(sol[i] * W[i] for i in range(len(W)) ))
        print ("Value:", sum(sol[i] * V[i] for i in range(len(W)) ))
    print("\n<TERMINADO>")
