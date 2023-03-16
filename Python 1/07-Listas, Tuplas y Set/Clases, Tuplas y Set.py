nombres = ['Edu', 'Juan', 'María', 'Pepe']

# Imprimir toda la lista
print(nombres)
# Un valor
print(nombres[2])
# En orden inverso
print(nombres[-3])
# Desde un valor a otro valor
print(nombres[1:3])
# Desde el principio hasta un valor
print(nombres[:2])
# Desde un valor hasta el final
print(nombres[1:])
# Para cambiar un elemento.
nombres[3] = 'Manolo'
print(nombres[3])
# Iterar una lista
for nombre in nombres:
    print(nombre)
# Ver longitud de la lista
print(len(nombres))
# Agregar un nuevo elemento
nombres.append('Rodri')
print(nombres)
# Insertar un elemento en un indice específico
nombres.insert(1,'Rubén')
print(nombres)
# Remover un elemento
nombres.remove('Rubén')
print(nombres)
# Remover el último elemento de la lista
nombres.pop()
print(nombres)
# Remover un índice
del nombres[0]
print(nombres)
# Limpiar todos los elementos de la lista
nombres.clear()
print(nombres)
# Eliminar la variable entera
del nombres
# TUPLAS: Es como una lista pero no se puede modificar, en vez de [] se usa (), si se puede imprimir rangos por ejemplo.
# Convertir tupla en lista
nombres = ('Edu', 'Ubaldo')
nombresLista = list(nombres)
# Convertir lista a tupla
nombres = tuple(nombresLista)
# SET: Es otro tipo de lista pero que no admite datos duplicados, se usa con {}, se pueden modificar los que hay dentro.
# Ver si un elemento se encuentra en una lista, tupla o set
planetas = {'Marte', 'Jupiter', 'Venus'}
print('Marte' in planetas)
# Insertar un nuevo elemento
planetas.add('Tierra')
print(planetas)
# Eliminar un elemento
planetas.discard('Tierra')
print(planetas)
# En los SET no existen los índices ya que se ordenan aleatoriamente
