# Definir una función e imprimir algo de dentro
def nombre():
    print('Hola mi nombres es:')


nombre()


# Usando valores
def suma(a, b):
    print(a + b)


suma(1, 2)


# Usando return
def suma(a, b):
    return a + b


resultado = suma(3, 4)
print(resultado)


# Usando argumentos (Cuando quiero usar un número indefinido de variables en mi función)(Crea una tupla)
def lista_nombres(*nombres):
    for nombre in nombres:
        print(nombre)


lista_nombres('PEPE', 'JUAN', 'MANOLO')


# Crear una función con diccionarios
def listar_terminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')


listar_terminos(PEPE='su significado', LOLA='Algo más')


# Añadir argumentos de una lista desde fuera de la función
def listar_nombres(names):
    for name in names:
        print(name)


names = ['Edu', 'Pepe', 'Juan']
listar_nombres(names)
