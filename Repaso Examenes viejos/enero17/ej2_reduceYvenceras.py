#a
#CON INDICES
def solve_indice(v, x):
    def aux(ini, fin):
        if fin - ini < 1:
            if v[ini] == x:
                return 1
            return 0
        else:
            # TODO no es  mitad = ((fin - ini) // 2), hay que sumarle el ini al usar indices
            mitad = ini + ((fin - ini) // 2)
            return aux(ini, mitad) + aux(mitad + 1, fin)

    return aux(0, len(v) - 1)

#CON SUB VECTORES
def solve(v, x):
    if len(v) == 1:
        if v[0] == x:
            return 1
        return 0
    else:
        mitad = len(v) // 2
        return solve(v[:mitad], x) + solve(v[mitad:], x)

#b DESCRIPCION
"""
El algoritmo recursivo divide el vector por la mitad para calcular recursivamente
cada mitad. Cuando la longitud del vector es igual a 1, es decir, solo queda un elemento,
se mira si ese elemento es el buscado y se devuelve 0 o 1. Cuando la longitud del vector
no es 1, se divide el vector por la mitad y se suma el resultado de la parte izquierda
y de la derecha.
"""

#c
"""
El coste temporal es:

       {    1                     si n = 1
T(n) = {    2 T(n/2) + O(n)       si n > 1
            
            --> El coste de las operaciones es O(n) pq hay operador de corte
            --> El coste recursivo es 2 T(n/2) pq hay dos llamadas a solve con la mitad
                del vector en cada una
            
    Como a = 2, b = 2, k = 1 y n = 0
        2 = 2^1 --> O(n*log(n))

El coste espacial es:
    -El tamaño de las variables del problema es un vector, por tanto O(n). 
    -Cada trama de activación tiene un coste espacial de O(n), ya que a cada 
        una se le pasa un vector nuevo. 
    -La profundidad máxima de la recursividad es de O(log n). 
    
    Por tanto, el coste espacial será de O(n*log n).
"""

if __name__ == '__main__':
    v = [-5, -5, 1, 1, 2, 2, 2, 2, 4, 4, 4, 7]

    print(solve_indice(v, 4))

    print(solve(v, 4))