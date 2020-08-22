def busca_indice_solitario(v):
    def rec(i, j):
        if j - i <= 1:
            return i

        medio = (i + j) // 2
        if v[medio] != v[medio-1] and v[medio] != v[medio+1]:
            return medio
        else:
            if medio % 2 == 0:
                if v[medio] == v[medio-1]:
                    return rec(i, medio)
                else:
                    return rec(medio+1, j)
            else:
                if v[medio] != v[medio-1]:
                    return rec(i, medio)
                else:
                    return rec(medio+1, j)

    return rec(0, len(v))

"""
Se obtiene el valor medio del vector. Si este es diferente de sus dos vecinos, se devuelve.

Si no, si este es diferente del de la izquierda
"""



if __name__ == '__main__':
    v = [1,1,2,2,3,3,4,4,5,5,6,7,7,8,8,9,9]

    pos = busca_indice_solitario(v)
    print(pos, v[pos]) #   Deberá mostrar: 4 3

