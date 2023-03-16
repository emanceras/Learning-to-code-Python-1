# Convertir un int a un str

numero = int(input("Introduce un numero del 1 al 3:"))
numeroTexto = ''
if numero == 1:
    numeroTexto = "uno"
elif numero == 2:
    numeroTexto = "dos"
elif numero == 3:
    numeroTexto = "tres"
else:
    print("No es un valor valido")
print(f'Numero proporcionado: {numero} - {numeroTexto}')
