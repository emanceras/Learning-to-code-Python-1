# Imprimir mensaje según etapa de la vida

edad = int(input("Introduce tu edad:"))
etapa = None

if 0 <= edad <= 9:
    etapa = "La infancia es increible..."
elif 10 <= edad <= 19:
    etapa = "Muchos cambios y mucho estudio..."
elif 20 <= edad <= 30:
    etapa = "Amor y comienza el trabajo..."
else:
    etapa = "Etapa de vida no reconocida"
print(etapa)