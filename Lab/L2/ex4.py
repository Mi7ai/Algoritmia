from Lab.L2.ex3 import cuadrado


def first(n, iter):
    cont = 0
    for i in iter:
        if cont<n:
            yield i
            cont +=1
        else:
            break


x = [1, 2, 10, 4, 5]
for n in first(3, cuadrado(x)):
    print(n)
for n in first(3, cuadrado(x)):
    print(n)