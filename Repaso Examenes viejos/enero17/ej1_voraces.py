#a
def menor_numero_intervalos(puntos: "[Float]", a: "Float") -> "Int":
    indices_ordenados = sorted(range(len(puntos)), key=lambda i: puntos[i])

    cant = 1
    inicio = puntos[indices_ordenados[0]]

    for i in indices_ordenados:
        if not inicio <= puntos[i] <= inicio + a:
            cant += 1
            # TODO MAL NO ES inicio = i
            inicio = puntos[i]

    return cant

# Descripcion del algoritmo:
""" 
Se ordenan los índices del vector de puntos en función del valor de los puntos,
de menor a mayor. Entonces, el primer intervalo se inicia en el valor del menor punto,
en el ejemplo, en el 1.0. A continuación, se recorren todos los indices ordenados y si 
el punto examinado no cabe entre el inicio del intervalo y el fin (inicio + a), se crea
un nuevo intervalo que se inicia en el punto actual. En el ejemplo, el 2.5 y el 3.5 entran
en el intervalo. Como el 7 no entra, se crea un nuevo intervalo que empieza en el 7.
"""

#b
# TODO REDUCCION A LA DIFERENCIA
"""
Cuando un punto no cabe en el intervalo actual, nosotros elegimos como inicio el valor
del punto, i. Suponemo que la solución optima coge otro distinto, j.

Hay dos opciones
    - j > i
        Con esta opción, i no cabia en el intervalo anterior, pero al crear un intervalo
        que se inicia en un punto más grande que i, i no entrara en ningun intervalo y 
        es erronea la solución.
    
    - j < i
        Con esta opción, el punto hasta el que llega el intervalo es más pequeño y con
        esto, esta solución no puede ganar a la nuestra, como mucho empatar.
"""

#c
""" 
El coste temporal es el de la ordenacion O(N lg(N))
El coste espacial es el del vector de indices O(N)
"""



if __name__ == '__main__':
    v = [1.0, 3.5, 9, 2.5, 7.0, 11.2, 13.2, 14.3]

    print(menor_numero_intervalos(v, 3.0))

