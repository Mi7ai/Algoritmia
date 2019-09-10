# copia de una lista
a = [1, 2, 3]
b = a[:]
# fin copia

list = []

while True:
    nr = int(input("Nr: "))
    if nr < 0:
        break
    list.append(nr)

list.sort()

for elem in list:
    print("{}".format(elem))

