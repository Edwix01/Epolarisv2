def obtener_clave(diccionario, lista):
    for clave, valores in diccionario.items():
        if set(lista).issubset(valores):
            return clave
    return None

# Diccionario dado
diccionario = {'10.0.1.1': ['10.0.1.2', '10.0.1.2'], '10.0.1.2': ['10.0.1.1', '10.0.1.1', '10.0.1.3'], '10.0.1.3': ['10.0.1.2', '10.0.1.4', '10.0.1.5'], '10.0.1.4': ['10.0.1.3', '10.0.1.5'], '10.0.1.5': ['10.0.1.3', '10.0.1.4']}

# Lista dada
lista = ['10.0.1.4', '10.0.1.5']

# Obtener la clave que tiene como valores los elementos de la lista
clave = obtener_clave(diccionario, lista)

if clave:
    print("La clave que posee como valores los elementos de la lista es:", clave)
else:
    print("No se encontró ninguna clave que tenga como valores los elementos de la lista.")
