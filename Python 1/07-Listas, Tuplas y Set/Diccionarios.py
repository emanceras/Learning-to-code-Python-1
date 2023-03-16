# DICCIONARIOS
# Ejemplo
diccionario = {
    'PEPE': 'Programa Especial de Programación Espacial',
    'Eduardo': 'Mi nombre',
    'Lola': 'El nombre de mi perra'
}

# Imprimir
print(diccionario)
# Longitud
print(len(diccionario))
# Imprimir un elemento
print(diccionario['PEPE'])
# Otra forma de imprimir
print(diccionario.get('PEPE'))
# Modificar un elemento
diccionario['PEPE'] = 'programa especial de programación espacial'
print(diccionario)
# Recorrer los elementos
for termino, valor in diccionario.items():
    print(termino, valor)
# Para imprimir solo el término
for termino in diccionario.keys():
    print(termino)
# Para imprimir solor el valor
for valor in diccionario.values():
    print(valor)
# Comprobar si existe ya un término en el diccionario
print('PEPE' in diccionario)
# Agregar un elemento al diccionario
diccionario['DNI'] = '53967319G'
# Remover un elemento
diccionario.pop('DNI')
# Eliminar todos los elementos sin borrar la variable
diccionario.clear()
# Eliminar el diccinario
del diccionario
