# Imprimir en pantalla los datos del libro que introduzca

print("Proporcione los siguientes datos del libro.")
nombre = input("Proporciona el nombre:")
identificador = int(input(f'Proporcione el ID:'))
precio = float(input(f'Proporcione el precio:'))
envioGratis = (input("Indique si el envio es gratuito (True/False)"))

if envioGratis == 'True':
    envioGratis = True
elif envioGratis == 'False':
    envioGratis = False
else:
    envioGratis = "Introduzca True o False"

print(f'''
Nombre: {nombre}
ID: {identificador}
Precio: {precio}
¿Envio gratuito?: {envioGratis}
''')