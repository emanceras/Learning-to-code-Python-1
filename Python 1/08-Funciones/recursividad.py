# Calcular un número factoriaL
def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)


resultado = factorial(5)
print(resultado)


# Imprimir del 5 al 1 de manera descendente usando recursividad
def descend(number):
    if 1 <= number <= 5:
        print(number)
        descend(number - 1)
    elif number == 0:
        return
    elif number < 0:
        print('ERROR')
    elif number > 5:
        print('ERROR')


descend(5)