# Imprimir calificación alfabética

nota = int(input("Introduce tu nota (0 al 10):"))
calificacion = ''

if 0 <= nota <= 4:
    calificacion = "F"
elif 5 <= nota <= 6:
    calificacion = "C"
elif 7 <= nota <= 8:
    calificacion = "B"
elif 9 <= nota <= 10:
    calificacion = "A"
else:
    calificacion = "calificacion erronea, introduce un valor del 0 al 10"

print(f'Tu nota {nota} es una {calificacion}')