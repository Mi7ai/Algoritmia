from typing import *
from random import random, seed


def mientras_quepa(W: List[int], C: int) -> List[int]:
    sol = []
    peso = 0
    contenedor = 0

    for w in W:
        if peso + w > C:#anadir otro contenedor
            contenedor += 1
            peso = 0
        peso += w
        sol.append(contenedor)
    return sol


def primero_que_quepa(W: List[int], C: int) -> List[int]:
    sol = []
    peso = []
    for w in W:
        encontrado = False
        for c in range(len(peso)):
            if peso[c] + w <= C:
                encontrado = True
                break
        if not encontrado:
            peso.append(0)
            c = len(peso)-1
        peso[c] += w
        sol.append(c)

    return sol

def primero_que_quepa2(W: List[int], C: int) -> List[int]:
    sol = []
    peso = []
    for w in W:
        for c in range(len(peso)):
            if peso[c] + w <= C:
                break
        else:
            peso.append(0)#peso del contenedor
            c = len(peso)-1#contenedor
        peso[c] += w
        sol.append(c)

    return sol


#no acabado
def primero_que_quepa_ordenado(W: List[int], C: int) -> List[int]:
    indices_ordenados = sorted(range(len(W)), key=lambda i: -W[i])
    sol = []
    peso = []

    for i in indices_ordenados:
        w = W[i]
        for c in range(len(peso)):
            if peso[c] + w <= C:
                break
        else:
            peso.append(0)
            c = len(peso)-1
        peso[c] += w
        sol.append(c)

    return sol

def prueba_binpacking():
    W, C = [1, 2, 8, 7, 8, 3], 10
    # seed(42)
    # W, C = [int(random()*1000)+1 for i in range(1000)], 1000

    for solve in [mientras_quepa, primero_que_quepa, primero_que_quepa2, primero_que_quepa_ordenado]:
        print("-" * 40)
        print("Método:", solve.__name__)
        try:
            sol = solve(W, C)
            print("Usados {} contenedores: {}".format(1 + max(sol), sol))
        except NotImplementedError:
            print("No implementado")


if __name__ == "__main__":
    prueba_binpacking()
