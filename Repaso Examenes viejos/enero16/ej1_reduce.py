def solve_indice(v):
    def solve(ini, fin):
        if fin - ini <= 1:
            return ini


        mitad = (fin + ini) // 2
        if v[mitad] < v[mitad + 1] and v[mitad] < v[mitad - 1]:
            return mitad


        # se busca uno.
        elif v[mitad] > v[mitad - 1]:
            return solve(ini, mitad)

        else:
            return solve(mitad+1, fin)

    return solve(0, len(v))

# Obtiene el valor del medio (si solo hay uno, obtiene ese) y si no es el primero ni el ultimo
# mira si es un minimo local y si lo es, lo devuelve.

# Si el valor medio no era un minimo local, mira a izquierda y derecha
    # Si el valor de la izquierda del medio es menor, se hace la recursivad por
    # la izquierda, ya que al ser menor al medio como tambien es menor al primero
    # de todos (enunciado), habra un minimo local en esa zona.

    # Si el de izquierda no era menor, lo sera el de la derecha, porque si fueran los
    # dos mayores ya habria encntrado un minimo. Entonces, como el de la derecha es menor
    # y tambien es menor que el ultimo, habra un minimo local en esa zona seguro,
    # aunque podria haber tambien en la otra, pero como solo se pide encontrar uno.



if __name__ == '__main__':
    v = [11, 9, 3, 8, 6, 5, 8, 9, 10]

    print(solve_indice(v))