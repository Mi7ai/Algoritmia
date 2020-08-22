# ASUMIMOS QUE beneficios y duraciones estan ordenadas por el ratio beneficio / duracion
# de mayor a menor

#MIENTRAS QUEPA CON ORDENACION
def cota_pes_subp(dias, beneficios, duraciones):
    beneficio = 0

    for i in range(len(beneficios)):
        if dias >= duraciones[i]:
            dias -= duraciones[i]
            beneficio += beneficios[i]

    return beneficio

#CON FRACCIONAMIENTO DE DIAS --> MIENTRAS QUEPA
def cota_opt_subp(dias, beneficios, duraciones):
    beneficio = 0

    for i in range(len(beneficios)):
        fraccion = min(1, dias / duraciones[i])
        beneficio += fraccion * beneficios[i]
        dias -= fraccion * duraciones[i]

    return beneficio