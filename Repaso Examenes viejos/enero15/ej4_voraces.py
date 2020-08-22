def algoritmo(X, D):
    sol = [X[0] + D]

    for c in X:
        #TODO NO GUARDAR VAR CON ULTIMO INDICE; USAR El -1
        guarda_actual = sol[-1]
        if c > guarda_actual + D:
            sol.append(c + D)

    return sol

if __name__ == '__main__':
    X = [2, 4, 7, 9, 12]
    D = 2

    print(algoritmo(X, D))


"""
Inicialmente, se pone un guardia D posiciones a la derecha del primer cuadro, para que cubra ese pero 
estando lo mas a la derecha posible. A continuación, se observa cada cuadro y si su posicion es superior
a la del ultimo guarda más D, se añade un nuevo guarda D posiciones a la derecha de el cuadro que se
esta observando.


COSTES

coste temporal --> O(X) recorre todos los cuadros
coste espacial --> solo almacena una lista con las posiciones de los guardias, por tanto O(1)


Por reduccion a la diferencia.
Nuestra solución difiere de una optima en la decision j (puede ser la primera). Por tanto, en 
esta decision hay dos opciones.

    sol[j] < sol_opt[j]
        Si la optima pone un guardia más a la derecha que nuestra solucion, tiene que ser erronea
        porque quedara algun cuadro sin cubrir, ya que nosotros lo hemos puesto lo maximo a la 
        derecha posible del cuadro que necesitaba guardia. Si por ejemplo hay un cuadro en 7, y 
        tenemos un guardia en 9, si la optima da una solucion en 10, el cuadro no estara cubierto, 
        porque las decisiones anteriores eran iguales.

    sol[j] > sol_opt[j]
        Si la optima pone un guardia mas a la izquierda que nuestra solucion, puede ser correcta
        pero no superara nuestra solucion, como mucho la igualara.       
"""