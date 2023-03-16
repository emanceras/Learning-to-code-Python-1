# Pruebas

# Imprimir cadena al revés
nombre = "Eduardo"

def invertir_cadena(cadena):
    return cadena[::-1]
print(invertir_cadena("\nHola"))

###############################

# Iterar cadena
cadena = "Hola Mundo\n"

for letra in cadena:
    print(letra)

###############################

# RANGE

for i in range(6):
    print(i, end=' ')  # El end en print se usa para quitar los saltos de linea que vienen por defecto en el for
print('\n')
# RANGE (Inicio, fin, salto)

for i in range(0, 6, 2):
    print(i,)
