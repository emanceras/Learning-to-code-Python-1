# Conertir de grados celsius a fahrenheit y al revés

elegir_conversion = \
    int(input("Introduce 1 para cambiar de Celsius a Fahrenheit o introduce 2 para cambiar de Fahrenheit "
                "a Celsius:"))


def conversor():
    if elegir_conversion == 1:
        temperatura = float(input("Introduce la temperatura:"))
        x = (temperatura * 9 / 5) + 32
        print(f'{x} ºF')
    elif elegir_conversion == 2:
        temperatura = float(input("Introduce la temperatura:"))
        y = (temperatura - 32) * 5 / 9
        print(f'{y} ºC')
    else:
        print("Introduce un valor válido.")


conversor()
