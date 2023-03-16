# Calcular si está en los 20 o en los 30

edadPersona = int(input('Introduce tu edad:'))
edadVeintes = 20 <= edadPersona < 30
edadTreintas = 30 <= edadPersona < 40

if edadVeintes or edadTreintas:
    print(f'Estás en el rango')
    if edadVeintes:
        print("Estas en los 20\'s")
    elif edadTreintas:
        print("Estás en los 30\'s")
else:
    print("No estás en ningún rango")
