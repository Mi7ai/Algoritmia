# no va
def pico(vec):
    if len(vec) == 1:
        return vec

    def p(v, i, j):
        c = (i+j)//2
        if i == j:
            return v[c]
        if v[c] < v[j]:  #voy a la derecha
            return p(v, c+1, j)
        if v[c] > v[i]:  #voy a la izquerda
            return p(v, i, c-1)

        return p(v, i, c-1)
    
    return p(vec, 0, len(vec)-1)

if __name__ == "__main__":
    v = [10, 20, 15, 2, 23, 90, 67]
    print(pico(v))