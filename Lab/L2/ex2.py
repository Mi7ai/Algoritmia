# generador para poner True en todos los numeros divisibles por 3

d = dict((i, i % 3 == 0) for i in range(1, 101))

for key, item in d.items():
    print(key, '->', item)
