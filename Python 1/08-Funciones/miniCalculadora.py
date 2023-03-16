# Crear un función que sume y acepte un número de argumentos variables

def suma(*numbers):
    total = 0
    for i in numbers:
        total += i
    return total


resultado = suma(1, 2, 3, 4)
print(resultado)


# Crear función que multiplique y acepte un número de argumentos variables

def multiplicar(*numbers):
    total = 1
    for i in numbers:
        total *= i
    return total


resultado = multiplicar(2, 3, 4)
print(resultado)
