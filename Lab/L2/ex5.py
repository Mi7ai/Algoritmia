def filter(cond, iter):
    for elem in iter:
        if cond(elem):
            yield elem

for n in filter(lambda n : n% 2 == 0, range(50, 100)):
    print(n)