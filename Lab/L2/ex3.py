def cuadrado(lista):
    for i in lista:
        yield i*i


x = [1, 2, 10, 4, 5]

for n in cuadrado(x):
    print(n)

#cuadrados.append(cuadrado(x))
#print(cuadrados[0])
