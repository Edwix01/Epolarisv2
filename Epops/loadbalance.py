l2 = [('10.0.1.2-3', '10.0.1.1-2'), ('10.0.1.2-4', '10.0.1.1-3'), ('10.0.1.3-3', '10.0.1.2-2'), ('10.0.1.3-2', '10.0.1.4-3'), ('10.0.1.3-4', '10.0.1.5-3'), ('10.0.1.4-2', '10.0.1.5-2')]
l1 = ['10.0.1.1-3', '10.0.1.5-2']


def gen_yaml(cone,dispblock,mapint):
    tuplas_encontradas = [tupla for tupla in cone if any(elemento in tupla for elemento in dispblock)]
    print(tuplas_encontradas)
    for tup in tuplas_encontradas:
        ip1 = (tup[0].split("-"))
        ip2 = (tup[1].split("-"))
        print(ip1[0],mapint[ip1[0]][ip1[1]])
        print(ip2[0],mapint[ip2[0]][ip2[1]])


gen_yaml(l2,l1,d)
