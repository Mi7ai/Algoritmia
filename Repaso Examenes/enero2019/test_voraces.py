def voraces(vector):
    v = sorted(range(len(vector)), key=lambda i: vector[i])
    suma = 0
    i = 0
    c = []
    while i < len(vector) - 1:
        coste = vector[v[i]] + vector[v[i + 1]]
        c.append(coste)
        suma += coste
        c.append(suma)
        i += 2
    c.append(suma + vector[v[len(v) - 1]])
    suma = 0
    for i in range(1, len(c)):
        #print(c[i])
        suma += c[i]

    return suma


if __name__ == '__main__':
    V = [14, 7, 6, 4, 9]
    V1 = [1, 2, 3, 4, 5]
    print(voraces(V))