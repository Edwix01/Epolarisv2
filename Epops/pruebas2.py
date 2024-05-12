l2 = [('10.0.1.2-3', '10.0.1.1-2'), ('10.0.1.2-4', '10.0.1.1-3'), ('10.0.1.3-3', '10.0.1.2-2'), ('10.0.1.3-2', '10.0.1.4-3'), ('10.0.1.3-4', '10.0.1.5-3'), ('10.0.1.4-2', '10.0.1.5-2')]
l1 = ['10.0.1.1-3', '10.0.1.5-2']
d = {'10.0.1.1': {'1': 'G0/1', '2': 'G0/2', '3': 'G0/3', '4': 'G1/0', '5': 'G1/1', '6': 'G1/2', '7': 'G1/3', '8': 'G2/0', '9': 'G2/1', '10': 'G2/2', '11': 'G2/3', '12': 'G3/0', '13': 'G3/1', '14': 'G3/2', '15': 'G3/3'}, '10.0.1.2': {'1': 'G0/1', '2': 'G0/2', '3': 'G0/3', '4': 'G1/0', '5': 'G1/1', '6': 'G1/2', '7': 'G1/3', '8': 'G2/0', '9': 'G2/1', '10': 'G2/2', '11': 'G2/3', '12': 'G3/0', '13': 'G3/1', '14': 'G3/2', '15': 'G3/3'}, '10.0.1.3': {'1': 'G0/1', '2': 'G0/2', '3': 'G0/3', '4': 'G1/0', '5': 'G1/1', '6': 'G1/2', '7': 'G1/3', '8': 'G2/0', '9': 'G2/1', '10': 'G2/2', '11': 'G2/3', '12': 'G3/0', '13': 'G3/1', '14': 'G3/2', '15': 'G3/3'}, '10.0.1.4': {'1': 'G0/1', '2': 'G0/2', '3': 'G0/3', '4': 'G1/0', '5': 'G1/1', '6': 'G1/2', '7': 'G1/3', '8': 'G2/0', '9': 'G2/1', '10': 'G2/2', '11': 'G2/3', '12': 'G3/0', '13': 'G3/1', '14': 'G3/2', '15': 'G3/3'}, '10.0.1.5': {'1': 'G0/1', '2': 'G0/2', '3': 'G0/3', '4': 'G1/0', '5': 'G1/1', '6': 'G1/2', '7': 'G1/3', '8': 'G2/0', '9': 'G2/1', '10': 'G2/2', '11': 'G2/3', '12': 'G3/0', '13': 'G3/1', '14': 'G3/2', '15': 'G3/3'}}

def ordenar_ip(l):
    ln = []    
    for i in l:
        ln.append(sorted(i))

    return ln


def eliminar_numeros(lista):
    # Función para eliminar los números después del guion en cada elemento de la lista
    def eliminar_numeros_item(item):
        return tuple(part.split('-')[0] for part in item)

    # Aplicar la función a cada elemento de la lista y devolver el resultado
    return [eliminar_numeros_item(item) for item in lista]

def generar_diccionario_conexiones(vector):
    diccionario_conexiones = {}
    
    for tupla in vector:
        for direccion in tupla:
            if direccion not in diccionario_conexiones:
                diccionario_conexiones[direccion] = []
        
        # Agregar las conexiones de cada dirección
        diccionario_conexiones[tupla[0]].append(tupla[1])
        diccionario_conexiones[tupla[1]].append(tupla[0])
    
    return diccionario_conexiones

def gen_yaml(cone,dispblock,mapint):
    tuplas_encontradas = [tupla for tupla in cone if any(elemento in tupla for elemento in dispblock)]
    for tup in tuplas_encontradas:
        ip1 = (tup[0].split("-"))
        ip2 = (tup[1].split("-"))
        print(ip1[0],mapint[ip1[0]][ip1[1]])
        print(ip2[0],mapint[ip2[0]][ip2[1]])

def obtener_clave(diccionario, lista):
    for clave, valores in diccionario.items():
        if set(lista).issubset(valores):
            return clave
    return None

def conteo_conex(lb,lc,cone,dis,map):
    c = 0
    for i in lb:
        if lc.count(i) >=2:
            gen_yaml(cone,dis[c],map)
        else:
            df = generar_diccionario_conexiones(lc)
            ni = obtener_clave(df,i)
            print(ni)
        c +=1 


a1 = (ordenar_ip(eliminar_numeros(l2)))
a2 = [tupla for tupla in l2 if any(elemento in tupla for elemento in l1)]
a2n = ordenar_ip(eliminar_numeros(a2))
conteo_conex(a2n,a1,l2,a2,d)
