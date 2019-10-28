# calcula distancia entre 2 puntos mediante la formula de la distancia de Manhattan
# formula x = (a,b), y = (c,d). La distancia entre x e y = |a-c|+|b-d|
def calcular_distancia_entre_celdas(u, v):
	a = u[0]
	b = u[1]
	c = v[0]
	d = v[1]

	distancia = abs(a - c) + abs(b - d)

	return distancia