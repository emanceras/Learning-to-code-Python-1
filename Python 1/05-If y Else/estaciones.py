# Calcular estación según mes

mesNumero = int(input("Introduce el mes (1 al 12):"))
mes = ''

if mesNumero == 12 or 1 <= mesNumero <= 2:
    mes = "Invierno"
elif 3 <= mesNumero <= 5:
    mes = "Primavera"
elif 6 <= mesNumero <= 8:
    mes = "Verano"
elif 9 <= mesNumero <= 11:
    mes = "Otoño"
else:
    mes = "erroneo, introduce un valor válido (1 al 12)"
print(f'El mes numero {mesNumero} es {mes}.')
