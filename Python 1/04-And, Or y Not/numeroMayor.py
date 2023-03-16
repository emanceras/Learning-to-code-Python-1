# Imprimir el número mayor de entre dos números

numero1 = int(input("Introduce el número1:"))
numero2 = int(input("Introduce el numero2:"))

numero1May = numero1 > numero2
numero2May = numero2 > numero1

if numero1May:
    print(f'El numero mayor es: {numero1}')
elif numero2May:
    print(f'El numero mayor es: {numero2}')
else:
    print("Son iguales")
